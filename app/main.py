from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import resume

app = FastAPI(
    title="AI Resume Critic",
    description="AI-powered resume analysis and ATS scoring",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)


@app.get("/")
def root():
    return {
        "message": "AI Resume Critic API is running"
    }
