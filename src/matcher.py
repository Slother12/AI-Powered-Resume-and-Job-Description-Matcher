import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def bert_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    vec1 = np.array([embeddings[0]])
    vec2 = np.array([embeddings[1]])
    sim = cosine_similarity(vec1, vec2)[0][0]
    return sim

def rank_resumes(resume_texts, jd_text):
    scores = []
    for text in resume_texts:
        score = bert_similarity(text, jd_text)
        scores.append(score)
    # Return indices of resumes sorted by score (highest first)
    return np.argsort(scores)[::-1], scores
