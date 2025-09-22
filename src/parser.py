import re
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def parse_pdf(file):
    text = extract_text(file)
    return text

def extract_skills(text, skill_list=None):
    text = text.lower()
    found_skills = []
    if skill_list:
        for skill in skill_list:
            if re.search(rf"\b{skill.lower()}\b", text):
                found_skills.append(skill)
    return found_skills

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()
