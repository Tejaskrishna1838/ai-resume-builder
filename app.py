import streamlit as st
import requests
import pdfkit

st.set_page_config(page_title="AI Resume Builder", layout="centered")

st.markdown("""
    <style>
    .title {
        font-size:32px;
        font-weight:bold;
        color:#4F8BF9;
        margin-bottom:10px;
    }
    .section-title {
        font-size:20px;
        font-weight:bold;
        margin-top:20px;
        color:#333;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI Resume Builder</div>', unsafe_allow_html=True)

# INPUT SECTIONS
name = st.text_input("👤 Full Name")
email = st.text_input("📧 Email")
education = st.text_area("🎓 Education")
experience = st.text_area("💼 Experience")
projects = st.text_area("📁 Projects")
skills = st.text_area("🛠️ Skills")
certifications = st.text_area("📜 Certifications")

# --- AI SUGGESTION FUNCTION ---
def query_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    except:
        return "❌ Failed to generate suggestion. Please try again later."

# --- SUGGESTION BUTTON ---
if st.button("✨ Generate AI Suggestions"):
    with st.spinner("Thinking..."):
        education = query_openrouter(f"Improve this education section:\n{education}")
        experience = query_openrouter(f"Improve this experience section:\n{experience}")
        projects = query_openrouter(f"Improve this project section:\n{projects}")
        skills = query_openrouter(f"Improve this skills section:\n{skills}")
        certifications = query_openrouter(f"Improve this certifications section:\n{certifications}")

    st.success("✅ Suggestions updated!")

    st.subheader("✨ Updated Sections")
    st.markdown(f"**🎓 Education:**\n\n{education}")
    st.markdown(f"**💼 Experience:**\n\n{experience}")
    st.markdown(f"**📁 Projects:**\n\n{projects}")
    st.markdown(f"**🛠️ Skills:**\n\n{skills}")
    st.markdown(f"**📜 Certifications:**\n\n{certifications}")

# --- JOB MATCHING / ATS SCORING ---
job_description = st.text_area("📝 Paste Job Description for ATS Scoring")
if st.button("🎯 Match Resume to Job"):
    if job_description:
        with st.spinner("Analyzing match..."):
            resume_summary = f"Name: {name}\nEmail: {email}\nEducation: {education}\nExperience: {experience}\nSkills: {skills}\nProjects: {projects}"
            feedback = query_openrouter(f"Score this resume against the job description. Provide ATS match score and suggestions:\nResume:\n{resume_summary}\n\nJob Description:\n{job_description}")
            st.subheader("🧠 ATS Feedback")
            st.write(feedback)
    else:
        st.warning("Please paste a job description first.")

# --- PDF EXPORT ---
if st.button("📥 Download Resume as PDF"):
    resume_html = f"""
    <h2>{name}</h2>
    <p><strong>Email:</strong> {email}</p>
    <h4>Education</h4><p>{education}</p>
    <h4>Experience</h4><p>{experience}</p>
    <h4>Projects</h4><p>{projects}</p>
    <h4>Skills</h4><p>{skills}</p>
    <h4>Certifications</h4><p>{certifications}</p>
    """
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_string(resume_html, "resume.pdf", configuration=config)
    with open("resume.pdf", "rb") as f:
        st.download_button("⬇️ Download PDF", f, file_name="resume.pdf")

