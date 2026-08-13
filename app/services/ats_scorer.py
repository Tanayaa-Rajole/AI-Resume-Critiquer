def calculate_ats_score(
    resume_text,
    keyword_score,
    section_score,
    experience_score
):

    score = (
        keyword_score * 0.4 +
        section_score * 0.3 +
        experience_score * 0.3
    )

    return round(score, 2)
