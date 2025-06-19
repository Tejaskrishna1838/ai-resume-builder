import streamlit as st
from utils import query_gemini, init_session

st.set_page_config(page_title="ATS Matcher", layout="centered")
init_session()

st.title("ATS Matcher")
st.write("Paste the job description below and click Match to analyze your resume.")

job_description = st.text_area("Job Description", value=st.session_state.job_description)

if st.button("Match with Resume"):
    with st.spinner("Analyzing your resume against the job description..."):
        summary = f"""Name: {st.session_state.resume_data['name']}
Email: {st.session_state.resume_data['email']}
Education: {st.session_state.resume_data['education']}
Experience: {st.session_state.resume_data['experience']}
Projects: {st.session_state.resume_data['projects']}
Skills: {st.session_state.resume_data['skills']}"""

        prompt = f"""Score this resume against the job description. 
Provide ATS match score (out of 100) and improvement suggestions.

Resume:
{summary}

Job Description:
{job_description}
"""

        ats_result = query_gemini(prompt)
        st.session_state.ats_result = ats_result

if st.session_state.ats_result:
    st.subheader("ATS Match Result")
    st.write(st.session_state.ats_result)
