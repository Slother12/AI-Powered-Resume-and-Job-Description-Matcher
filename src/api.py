from .parser import parse_pdf, extract_skills, clean_text
from .matcher import bert_similarity, rank_resumes
from .utils import highlight_skills

from fastapi import FastAPI, UploadFile, File
app = FastAPI(title="AI Resume-JD Matcher")

SKILL_LIST = ["Python", "Java", "SQL", "Machine Learning", "NLP", "Deep Learning"]

@app.post("/match")
async def match_resume(jd: UploadFile = File(...), resumes: list[UploadFile] = File(...)):
    jd_text = clean_text(parse_pdf(jd.file))
    jd_skills = extract_skills(jd_text, SKILL_LIST)

    results = []
    resume_texts = []
    for r in resumes:
        text = clean_text(parse_pdf(r.file))
        skills = extract_skills(text, SKILL_LIST)
        resume_texts.append(text)
        skill_info = highlight_skills(skills, jd_skills)
        results.append({
            "resume_name": r.filename,
            "matched_skills": skill_info["matched"],
            "missing_skills": skill_info["missing"]
        })

    order, scores = rank_resumes(resume_texts, jd_text)
    ranked_results = [results[i] | {"score": float(scores[i])} for i in order]

    return {"jd_skills": jd_skills, "ranked_resumes": ranked_results}

@app.get("/health")
def health():
    return {"status": "ok"}
