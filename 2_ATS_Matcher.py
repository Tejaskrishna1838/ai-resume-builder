import streamlit as st
from utils import query_deepseek, init_session
import pdfkit

st.set_page_config(page_title="ATS Matcher", layout="centered")

# Load styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Init session + resume
init_session()
resume = st.session_state.resume_data

st.title("ATS Score & Job Match")
st.markdown("Compare your resume with a job description and receive feedback to improve alignment.")

# ATS Match Section
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Job Description")
job_description = st.text_area("Paste the full job description here", height=300)
st.markdown("</div>", unsafe_allow_html=True)

# Match button
if st.button("Analyze Match"):
    if job_description.strip() == "":
        st.warning("Please paste a job description first.")
    else:
        with st.spinner("Analyzing your resume against the job description..."):
            resume_summary = f"""
Name: {resume['name']}
Email: {resume['email']}
Education: {resume['education']}
Experience: {resume['experience']}
Projects: {resume['projects']}
Skills: {resume['skills']}
Certifications: {resume['certifications']}
"""
            prompt = f"""
Evaluate the following resume against the job description.
Return:
1. ATS match score (0–100)
2. 3–5 bullet point suggestions for improving alignment

Resume:
{resume_summary}

Job Description:
{job_description}
"""
            feedback = query_deepseek(prompt)
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("ATS Feedback")
            st.markdown(feedback)
            st.markdown("</div>", unsafe_allow_html=True)

# PDF Download Option
if st.button("Download Resume as PDF"):
    resume_html = f"""
    <html><head><style>
        body {{ font-family: Poppins, sans-serif; color: #333; }}
        h2 {{ color: #4F8BF9; }}
        section {{ margin-bottom: 20px; }}
    </style></head><body>
        <h2>{resume['name']}</h2>
        <p><strong>Email:</strong> {resume['email']}</p>
        <section><h3>Education</h3><p>{resume['education']}</p></section>
        <section><h3>Experience</h3><p>{resume['experience']}</p></section>
        <section><h3>Projects</h3><p>{resume['projects']}</p></section>
        <section><h3>Skills</h3><p>{resume['skills']}</p></section>
        <section><h3>Certifications</h3><p>{resume['certifications']}</p></section>
    </body></html>
    """

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    )
    pdfkit.from_string(resume_html, "resume.pdf", configuration=config)
    with open("resume.pdf", "rb") as f:
        st.download_button("Download PDF", f, file_name="resume.pdf", mime="application/pdf")
