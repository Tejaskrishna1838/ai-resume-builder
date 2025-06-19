import streamlit as st
from utils import query_gemini, init_session

st.set_page_config(page_title="Resume Builder", layout="centered")
init_session()

st.title("Resume Builder")
st.write("Fill in your resume sections below and click Improve Sections to enhance them.")

resume = st.session_state.resume_data

with st.form("resume_form"):
    st.subheader("Personal Details")
    resume["name"] = st.text_input("Full Name", value=resume["name"])
    resume["email"] = st.text_input("Email", value=resume["email"])

    st.subheader("Education")
    resume["education"] = st.text_area("Describe your education background", value=resume["education"])

    st.subheader("Experience")
    resume["experience"] = st.text_area("List your work or internship experience", value=resume["experience"])

    st.subheader("Projects")
    resume["projects"] = st.text_area("Mention any projects you've worked on", value=resume["projects"])

    st.subheader("Skills")
    resume["skills"] = st.text_area("List your technical and soft skills", value=resume["skills"])

    st.subheader("Certifications")
    resume["certifications"] = st.text_area("Mention any certifications", value=resume["certifications"])

    submitted = st.form_submit_button("Improve Sections")

if submitted:
    with st.spinner("Enhancing with AI..."):
        resume["education"] = query_gemini(f"Improve this education section:\n{resume['education']}")
        resume["experience"] = query_gemini(f"Improve this experience section:\n{resume['experience']}")
        resume["projects"] = query_gemini(f"Improve this project section:\n{resume['projects']}")
        resume["skills"] = query_gemini(f"Improve this skills section:\n{resume['skills']}")
        resume["certifications"] = query_gemini(f"Improve this certifications section:\n{resume['certifications']}")

    st.success("Sections enhanced successfully!")
    st.subheader("Preview of Improved Sections")
    st.markdown(f"**Full Name:** {resume['name']}")
    st.markdown(f"**Email:** {resume['email']}")
    st.markdown(f"**Education:**\n{resume['education']}")
    st.markdown(f"**Experience:**\n{resume['experience']}")
    st.markdown(f"**Projects:**\n{resume['projects']}")
    st.markdown(f"**Skills:**\n{resume['skills']}")
    st.markdown(f"**Certifications:**\n{resume['certifications']}")
