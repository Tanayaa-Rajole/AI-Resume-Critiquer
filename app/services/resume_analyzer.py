def analyze_resume(text):

    sections = {
        "experience": False,
        "education": False,
        "skills": False,
        "projects": False,
        "certifications": False
    }

    lower_text = text.lower()

    for section in sections:
        if section in lower_text:
            sections[section] = True

    section_score = (
        sum(sections.values()) /
        len(sections)
    ) * 100

    return {
        "sections": sections,
        "section_score": round(section_score, 2)
    }
