import re


def extract_keywords(text: str):

    words = re.findall(r"\b[a-zA-Z][a-zA-Z+#.]+\b", text.lower())

    stop_words = {
        "the",
        "and",
        "for",
        "with",
        "from",
        "this",
        "that",
        "have",
        "has",
        "are",
        "was",
        "were",
        "will",
        "you",
        "your"
    }

    keywords = [
        word
        for word in words
        if word not in stop_words
    ]

    return set(keywords)


def calculate_keyword_match(resume_text, job_description):

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    if not job_keywords:
        return {
            "match_percentage": 0,
            "matched_keywords": [],
            "missing_keywords": []
        }

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords - resume_keywords

    score = (len(matched) / len(job_keywords)) * 100

    return {
        "match_percentage": round(score, 2),
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing)
    }
