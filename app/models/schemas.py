from pydantic import BaseModel
from typing import List


class ResumeAnalysis(BaseModel):

    overall_score: float

    keyword_match: float

    section_score: float

    experience_score: float

    matched_keywords: List[str]

    missing_keywords: List[str]

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]
