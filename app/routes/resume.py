import os
import google.generativeai as genai


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def analyze_with_ai(resume_text, job_description):

    prompt = f"""
You are an expert technical recruiter and resume reviewer.

Analyze the following resume.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return:

1. Resume strengths
2. Resume weaknesses
3. Missing technical skills
4. Missing keywords
5. Weak bullet points
6. Improved bullet points
7. ATS recommendations
8. Overall resume score from 0-100

Be specific and avoid generic advice.
"""

    response = model.generate_content(prompt)

    return response.text
