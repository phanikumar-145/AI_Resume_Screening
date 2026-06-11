import streamlit as st
from utils import extract_resume_text
from ml_model import calculate_match_score, get_candidate_status

# Page Configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 AI-Powered Resume Screening System")
st.write(
    "Upload a candidate resume and compare it with a job description to determine suitability."
)

# Job Description Input
job_description = st.text_area(
    "Enter Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

# Resume Upload
uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Analyze Button
if st.button("Analyze Resume"):

    # Validation
    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a job description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        # Extract Resume Text
        resume_text = extract_resume_text(uploaded_resume)

        # Calculate Match Score
        match_score = calculate_match_score(
            resume_text,
            job_description
        )

        # Determine Suitability
        status = get_candidate_status(match_score)

    st.success("Analysis Completed Successfully!")

    # Display Results
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Match Score",
            value=f"{match_score}%"
        )

    with col2:
        st.metric(
            label="Candidate Status",
            value=status
        )

    # Resume Preview
    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text[:5000],
        height=300
    )