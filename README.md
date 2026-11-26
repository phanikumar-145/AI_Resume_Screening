# AI Resume Screening System

An AI-assisted Resume Screening System built using Python, Streamlit, PyMuPDF, and machine learning-related libraries. The application analyzes PDF resumes against job descriptions, identifies matching technical skills, calculates a resume match score, and displays a candidate suitability status.

## Project Overview

Recruiters often receive a large number of resumes for a single job opening. Manually reviewing every resume and comparing candidate skills with job requirements can be time-consuming.

This project simplifies the initial screening process by extracting text from uploaded PDF resumes and comparing the extracted information with a given job description.

The application calculates a skill match percentage and classifies candidates into three categories: Selected, Shortlisted, or Rejected.

## Key Features

- Upload candidate resumes in PDF format.
- Enter a job description for comparison.
- Extract text from PDF documents using PyMuPDF.
- Identify technical skills mentioned in the job description.
- Compare required skills with skills found in the resume.
- Calculate a resume match percentage.
- Display candidate suitability status.
- Preview extracted resume text.
- Provide an interactive Streamlit interface.
- Validate resume uploads and job description inputs.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive user interface |
| PyMuPDF | PDF text extraction |
| Scikit-learn concepts | Foundation for future ML improvements |
| Sentence Transformers | Installed dependency for potential semantic matching |
| PyTorch | Deep learning library dependency |

Note: The current matching implementation uses predefined skill keywords and exact text matching. It does not currently use a trained machine learning model or semantic similarity embeddings.

## Project Architecture

```text
              User
               |
               |
       Streamlit Interface
               |
               |
        Enter Job Description
               |
               |
          Upload Resume
               |
               |
        PDF Text Extraction
               |
               |
             PyMuPDF
               |
               |
        Extracted Resume Text
               |
               |
        Skill Matching Logic
               |
               |
       Compare Required Skills
               |
               |
        Calculate Match Score
               |
               |
       Determine Candidate Status
               |
               |
         Display Results
```

## Project Structure

```text
AI_Resume_Screening/
|
|-- app.py
|-- ml_model.py
|-- utils.py
|-- requirements.txt
|-- __pycache__/
```

### Main Files

**app.py**

Contains the Streamlit frontend. It allows users to enter a job description, upload a PDF resume, start the analysis, and view the match score and candidate status.

**ml_model.py**

Contains the resume matching logic. It identifies predefined technical skills in the job description and resume, calculates the match percentage, and determines the candidate status.

**utils.py**

Contains the PDF text extraction function implemented using PyMuPDF.

**requirements.txt**

Contains the Python libraries required to run the application.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/phanikumar-145/AI_Resume_Screening.git
```

Navigate to the project directory:

```bash
cd AI_Resume_Screening
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application will open in your default browser.

## How to Use the Application

1. Start the Streamlit application.
2. Enter the job description in the text area.
3. Upload a candidate resume in PDF format.
4. Click the Analyze Resume button.
5. Wait for the resume text extraction and skill comparison.
6. View the calculated match percentage.
7. Review the candidate suitability status.
8. Examine the extracted resume text.

## Resume Matching Methodology

The application uses a predefined list of technical skills to compare resumes with job descriptions.

### Step 1: Resume Text Extraction

PyMuPDF extracts text from the uploaded PDF document.

### Step 2: Skill Identification

The application checks for predefined skills in the job description.

Examples include:

- Python
- SQL
- Machine Learning
- Deep Learning
- TensorFlow
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- NLP
- Generative AI
- LangChain
- FastAPI
- Streamlit
- PostgreSQL
- MongoDB
- React
- JavaScript

### Step 3: Skill Matching

The extracted resume text and job description are converted to lowercase.

The application checks which required skills appear in the resume.

### Step 4: Match Score Calculation

The match score is calculated using:

```python
match_score = (
    len(matched_skills) / len(required_skills)
) * 100
```

Where:

- Required Skills: Skills identified in the job description.
- Matched Skills: Required skills also found in the resume.

### Step 5: Candidate Classification

The application assigns candidate status based on the match score.

| Match Score | Candidate Status |
|---|---|
| 80% and above | Selected |
| 60% to below 80% | Shortlisted |
| Below 60% | Rejected |

If the job description contains no recognized skills, the application returns a score of zero.

## Example

### Job Description

```text
We are looking for a Python developer with experience
in SQL, Machine Learning, Pandas, NumPy, and FastAPI.
```

### Resume Skills

```text
Python
SQL
Machine Learning
Pandas
NumPy
```

### Example Result

| Required Skill | Resume Match |
|---|---|
| Python | Matched |
| SQL | Matched |
| Machine Learning | Matched |
| Pandas | Matched |
| NumPy | Matched |
| FastAPI | Not Matched |

Match Score: 83.33%

Candidate Status: Selected

This is an illustrative example of the matching calculation.

## Future Improvements

- Implement semantic similarity using Sentence Transformers.
- Add skill extraction using NLP techniques.
- Support multiple resume uploads.
- Rank candidates based on match scores.
- Extract education and work experience.
- Identify missing skills for each candidate.
- Support DOCX resume uploads.
- Add downloadable screening reports.
- Store candidate information in a database.
- Add recruiter dashboards and candidate filtering.
- Introduce explainable matching results.
- Evaluate matching quality using labeled resume and job-description datasets.

## Important Note

This application is designed as an initial resume-screening aid. Its keyword-based matching score should not be treated as a definitive measure of candidate ability or suitability.

Recruiters should review the complete resume and assess candidates using consistent, job-related criteria. The automated status should not be used as the sole basis for hiring decisions.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145

## Project Purpose

This project demonstrates practical implementation of PDF processing, text extraction, keyword-based skill matching, percentage-based scoring, and interactive application development using Python and Streamlit.
