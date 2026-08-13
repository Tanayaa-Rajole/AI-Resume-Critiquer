# 🤖 AI Resume Critic

An AI-powered resume analysis platform that evaluates resumes for **ATS compatibility, job relevance, technical skills, structure, and overall quality**.

AI Resume Critic helps students and job seekers understand what is weakening their resume and what they should improve before applying for a role.

---

## 🚀 Features

### 📄 Resume Parsing

* Upload PDF or DOCX resumes
* Extract resume text automatically
* Detect major resume sections
* Clean and preprocess extracted content

### 🎯 ATS Analysis

* Generate an ATS compatibility score
* Identify missing keywords
* Analyze resume structure
* Evaluate section completeness

### 💼 Job Description Matching

Paste a job description and compare it against the resume.

The system identifies:

* Matching skills
* Missing skills
* Relevant keywords
* Potential gaps
* Overall job-match percentage

### 🧠 AI Resume Critique

The AI analyzes the resume and provides:

* Strengths
* Weaknesses
* Missing technical skills
* Weak resume bullets
* Improvement suggestions
* ATS recommendations
* Overall resume score

### ✍️ Bullet Point Improvement

The system can identify weak or generic resume bullets and suggest stronger alternatives using specific actions, technologies, and measurable impact.

### 📊 Resume Dashboard

The frontend presents the analysis through an easy-to-understand dashboard containing:

* Overall score
* ATS score
* Skills match
* Experience score
* Missing keywords
* AI feedback
* Improvement recommendations

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │   Resume Upload  │
                    │    PDF / DOCX    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Resume Parser   │
                    │ PyMuPDF / DOCX   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Text Cleaning   │
                    └────────┬─────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │  ATS Analyzer   │     │   AI Analyzer   │
        │                 │     │     Gemini      │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 └───────────┬───────────┘
                             ▼
                    ┌──────────────────┐
                    │ Scoring Engine   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Analysis Report  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Dashboard     │
                    └──────────────────┘
```

---

# 🛠️ Tech Stack

| Layer           | Technology            |
| --------------- | --------------------- |
| Frontend        | HTML, CSS, JavaScript |
| Backend         | Python, FastAPI       |
| AI              | Google Gemini API     |
| PDF Processing  | PyMuPDF               |
| DOCX Processing | python-docx           |
| NLP             | spaCy                 |
| Data Validation | Pydantic              |
| Testing         | pytest                |
| Version Control | Git & GitHub          |

---

# 📁 Project Structure

```text
ai-resume-critic/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── resume.py
│   │   └── analysis.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   ├── resume_analyzer.py
│   │   ├── ats_scorer.py
│   │   ├── keyword_matcher.py
│   │   └── llm_service.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── text_cleaner.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_parser.py
│   ├── test_scorer.py
│   └── test_analyzer.py
│
├── uploads/
│   └── .gitkeep
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-resume-critic.git

cd ai-resume-critic
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install the spaCy model

```bash
python -m spacy download en_core_web_sm
```

## 5. Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your `.env` file to GitHub.

---

# ▶️ Running the Application

Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

Open the frontend:

```text
frontend/index.html
```

Then upload a resume and optionally provide a job description.

---

# 📊 Example Analysis

```text
Overall Score: 82/100

ATS Compatibility: 86%
Skills Match: 81%
Experience: 78%
Structure: 91%

Matched Skills:
✓ Python
✓ Java
✓ Git
✓ REST APIs
✓ Machine Learning

Missing Keywords:
⚠ Docker
⚠ MongoDB
⚠ Kubernetes

AI Recommendations:

1. Quantify project impact where possible.
2. Replace generic project descriptions with
   action-oriented bullet points.
3. Add relevant technical keywords from the
   target job description.
4. Strengthen the professional summary.
```

---

# 🧠 How the AI Analysis Works

The system follows a multi-stage pipeline:

### 1. Document Processing

The uploaded resume is converted into machine-readable text.

### 2. Resume Analysis

The extracted text is analyzed for:

* Resume sections
* Skills
* Experience
* Education
* Projects
* Certifications

### 3. Keyword Analysis

The resume is compared against the supplied job description.

Keywords are classified into:

```text
Matched Keywords
Missing Keywords
Potentially Relevant Keywords
```

### 4. ATS Scoring

Multiple signals are combined to calculate an overall resume score.

Example:

```text
Keyword Relevance      40%
Section Completeness   30%
Experience Relevance   30%
```

### 5. AI Critique

The resume and job description are passed to the LLM for contextual analysis.

The AI generates:

* Strengths
* Weaknesses
* Recommendations
* Missing skills
* Improved bullet points

---

# 🔮 Future Improvements

The project is designed to evolve beyond basic keyword matching.

Planned improvements include:

* [ ] Semantic similarity between resume and job description
* [ ] Advanced skill extraction
* [ ] Named Entity Recognition
* [ ] Experience-level detection
* [ ] Quantified achievement detection
* [ ] Resume section classification
* [ ] AI-generated resume summaries
* [ ] AI bullet-point rewriting
* [ ] Job-specific resume optimization
* [ ] Multiple resume version comparison
* [ ] Resume scoring history
* [ ] User accounts
* [ ] Resume improvement tracking
* [ ] Interactive analytics dashboard
* [ ] Deployment to the cloud
* [ ] Automated testing and CI/CD

---

# 🔐 Privacy

Resume documents may contain sensitive personal information.

The application should:

* Avoid storing resumes unnecessarily
* Never expose uploaded resumes publicly
* Keep API keys in environment variables
* Exclude uploaded documents from Git
* Delete temporary files after processing where possible

---

# 🧪 Testing

Run the test suite using:

```bash
pytest
```

Tests cover:

* Resume text extraction
* Keyword matching
* ATS scoring
* Resume section detection
* Analysis logic

---

# 🌐 API

### Analyze Resume

```http
POST /api/resume/analyze
```

### Request

```text
resume: PDF or DOCX file
job_description: Optional text
```

### Response

```json
{
  "resume_analysis": {
    "section_score": 91
  },
  "keyword_analysis": {
    "match_percentage": 84,
    "matched_keywords": [],
    "missing_keywords": []
  },
  "ai_analysis": "..."
}
```

---

# 🎯 Project Goals

The primary goals of AI Resume Critic are to:

1. Make resume feedback accessible to students and early-career developers.
2. Provide job-specific rather than generic resume recommendations.
3. Combine traditional resume scoring with LLM-based analysis.
4. Help users identify missing skills and keywords.
5. Demonstrate practical implementation of AI in a real-world application.

---

# 👩‍💻 Author

**Tanayaa**

Engineering Student | AI & ML | Software Development

---

# ⭐ Contributing

Contributions are welcome.

To contribute:

```bash
git checkout -b feature/new-feature

git add .

git commit -m "Add new feature"

git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

```
```
