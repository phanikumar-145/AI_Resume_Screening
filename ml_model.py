# ml_model.py

def calculate_match_score(resume_text, job_description):

    skills = [
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
        "express.js"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    required_skills = []
    matched_skills = []

    for skill in skills:

        if skill in job_description:
            required_skills.append(skill)

            if skill in resume_text:
                matched_skills.append(skill)

    if len(required_skills) == 0:
        return 0

    # Exact skill match percentage
    skill_score = (len(matched_skills) / len(required_skills)) * 100

    print("Required Skills:", required_skills)
    print("Matched Skills:", matched_skills)
    print("Skill Score:", skill_score)

    return round(skill_score, 2)


def get_candidate_status(score):

    if score >= 80:
        return "Selected"

    elif score >= 60:
        return "Shortlisted"

    else:
        return "Rejected"