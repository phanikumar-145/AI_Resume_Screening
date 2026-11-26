# ml_model.py

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "git",
    "github",
    "rest api",
    "data structures",
    "algorithms",
    "oop",
    "nlp",
    "generative ai",
    "langchain",
    "fastapi",
    "streamlit",
    "mongodb",
    "mysql",
    "postgresql",
    "data analysis",
    "statistics",
    "power bi",
    "excel",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "express.js",
]


def calculate_match_score(resume_text: str, job_description: str) -> float:
    """
    Calculate a basic keyword-based resume match percentage.

    Only skills detected in the job description are treated as required.
    The score is the percentage of those required skills also found in
    the resume, so the result remains between 0 and 100.
    """
    resume_text = (resume_text or "").lower()
    job_description = (job_description or "").lower()

    required_skills = [
        skill for skill in SKILLS if skill in job_description
    ]

    if not required_skills:
        return 0.0

    matched_skills = [
        skill for skill in required_skills if skill in resume_text
    ]

    score = (len(matched_skills) / len(required_skills)) * 100
    return round(score, 2)


def get_candidate_status(score: float) -> str:
    """Return the project's demonstration category for a match score."""
    if score >= 80:
        return "Selected"
    if score >= 60:
        return "Shortlisted"
    return "Rejected"
