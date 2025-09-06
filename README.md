# AI-Powered-Resume-and-Job-Description-Matcher
AI-Powered Resume and Job Description Matcher using NLP and Semantic Similarity – A system that parses resumes &amp; JDs, extracts skills, and matches candidates to jobs with explainable insights.

# AI-Powered Resume and Job Description Matcher (Self Project)

This is a **self-initiated project** where I built an AI-powered system to match resumes with job descriptions using **Natural Language Processing (NLP)** and **semantic similarity**.  
The project simulates a simplified version of an **Applicant Tracking System (ATS)** by parsing resumes and JDs, extracting important skills/experience, and ranking candidates with explainable results.  

## link to repository
-- https://github.com/Slother12/AI-Powered-Resume-and-Job-Description-Matcher

---

## What I Learned
- Applying **TF-IDF** and **Sentence-BERT embeddings** for semantic similarity.  
- Designing an end-to-end **data pipeline** for text parsing, cleaning, and feature extraction.  
- Building a **FastAPI service** to make the matcher usable as an API.  
- Improving interpretability by highlighting **matched vs missing skills** in results.  

---

## Tech Stack
- **Languages:** Python  
- **Libraries:** Scikit-learn, Transformers (Sentence-BERT), Pandas, NumPy, NLTK, SpaCy  
- **Frameworks:** FastAPI  
- **Indexing/Storage:** FAISS (for similarity search)  
- **Other Tools:** Docker, GitHub  
---

## What the Project Does

This project works like a **mini Applicant Tracking System (ATS)** to evaluate how well a resume matches a job description.

- **Resume & JD Parsing** → Reads PDF/TXT files and extracts skills, experience, and keywords.  
- **Semantic Similarity** → Uses TF-IDF and Sentence-BERT embeddings with cosine similarity to measure match strength.  
- **Explainable Insights** → Highlights matched and missing skills, providing transparency into the scoring.  
- **Candidate Ranking** → Scores and ranks multiple resumes against a given JD for recruiter efficiency.  
- **Practical Use Case** → Helps both recruiters (for shortlisting) and candidates (to identify skill gaps).  

---
## ⚙️ How to Run
  -- Clone the repo
  -- git clone https://github.com/your-username/resume-jd-matcher.git
  -- cd resume-jd-matcher
   
## Install requirements
  -- pip install -r requirements.txt

## Run the API server
  -- uvicorn src.api:app --reload
## Future Work

 -- Adding a UI for recruiters to upload resumes & JDs.

 -- Multi-language resume parsing.

 -- Experimenting with fine-tuned transformer models.





