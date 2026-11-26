# AI Resume Screening System

A Streamlit application that extracts text from PDF resumes and compares the extracted content with a job description. It uses a predefined list of technical skills and keyword matching to calculate a simple match percentage.

## Features

- Upload a resume in PDF format.
- Enter a job description.
- Extract text from the uploaded PDF using PyMuPDF.
- Identify skills mentioned in the job description.
- Compare those skills with the extracted resume text.
- Display a match percentage and a rule-based candidate category.
- Preview the extracted resume text.

## Technology Stack

- Python
- Streamlit
- PyMuPDF
- Regular-expression-free keyword matching

## Project Structure

```text
AI_Resume_Screening/
├── app.py
├── ml_model.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How the Application Works

1. The user enters a job description and uploads a PDF resume.
2. `utils.py` extracts text from the PDF using PyMuPDF.
3. `ml_model.py` checks which predefined skills appear in the job description and resume.
4. The application calculates a match percentage from the number of matching required skills.
5. Streamlit displays the score, category, and extracted resume text.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/phanikumar-145/AI_Resume_Screening.git
cd AI_Resume_Screening
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser.

## Match Score Logic

The current implementation uses a predefined list of skills such as Python, SQL, machine learning, FastAPI, React, and PostgreSQL.

The match score is calculated as:

```text
Match Score = (Number of required skills found in the resume
               / Number of skills found in the job description) * 100
```

Only skills identified in the job description are considered required skills. This keeps the score within the expected 0–100 range.

The displayed candidate category is based on fixed thresholds in `ml_model.py`:

- 80% and above: Selected
- 60% to below 80%: Shortlisted
- Below 60%: Rejected

These labels are simple demonstration rules, not validated hiring criteria.

## Limitations

- This is a keyword-matching project, not a trained machine-learning or semantic-understanding model.
- It may miss synonyms, related skills, context, and experience depth.
- A skill can be counted even if it appears in an unrelated context.
- Image-only or scanned PDFs may not provide extractable text unless OCR is added.
- The skill list is predefined in `ml_model.py` and may need to be updated for different job roles.
- The match score should not be used as the sole basis for hiring decisions. A human reviewer should evaluate each application.

## Possible Improvements

- Add OCR support for scanned resumes.
- Use semantic similarity or embeddings to compare resume content with job requirements.
- Extract skills, education, and experience into structured fields.
- Add tests for PDF extraction and scoring.
- Add file-size limits and clearer handling for encrypted, corrupted, or empty PDFs.
- Allow recruiters to customize the skills list and scoring weights.
