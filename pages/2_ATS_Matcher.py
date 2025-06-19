import streamlit as st
from utils import query_deepseek, init_session

st.set_page_config(page_title="ATS Matcher", layout="centered")

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session
init_session()
resume = st.session_state.resume_data

st.title("ATS Matcher")
st.markdown("Paste a job description and compare it with your resume to get match score and improvement tips.")

with st.form("ats_form"):
    st.subheader("Job Description")
    job_description = st.text_area("Paste the full job description below", height=200)

    submitted = st.form_submit_button("Analyze Match")
    if submitted:
        if not job_description.strip():
            st.warning("Please enter a valid job description.")
        elif not resume or not resume.get("experience"):
            st.warning("Please fill out your resume on the Resume Builder page first.")
        else:
            with st.spinner("Matching resume to job description..."):
                resume_text = f"""
Name: {resume['name']}
Email: {resume['email']}
Education: {resume['education']}
Experience: {resume['experience']}
Projects: {resume['projects']}
Skills: {resume['skills']}
Certifications: {resume['certifications']}
"""

                prompt = f"""
Compare the resume below to the job description. 
Give an ATS score out of 100 and provide improvement suggestions:

Resume:
{resume_text}

Job Description:
{job_description}
"""

                feedback = query_deepseek(prompt)

            st.markdown("---")
            st.subheader("Match Feedback")
            st.code(feedback, language="markdown")
