import streamlit as st
from utils import query_deepseek, init_session

st.set_page_config(page_title="Resume Builder", layout="centered")

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
init_session()
resume = st.session_state.resume_data

st.title("Resume Builder")
st.markdown("Fill in your resume sections below and click 'Improve Sections' to enhance them.")

# --- Resume Form ---
with st.form("resume_form"):

    st.subheader("Personal Details")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value=resume.get("name", ""), key="name_input")
        with col2:
            st.text_input("Email", value=resume.get("email", ""), key="email_input")

    st.divider()

    st.subheader("Education")
    st.text_area("Describe your academic background", value=resume.get("education", ""), height=140, key="education_input")

    st.divider()

    st.subheader("Experience")
    st.text_area("List your relevant work or internship experiences", value=resume.get("experience", ""), height=140, key="experience_input")

    st.divider()

    st.subheader("Projects")
    st.text_area("Include key personal or academic projects", value=resume.get("projects", ""), height=140, key="projects_input")

    st.divider()

    st.subheader("Skills")
    st.text_area("Mention your technical and soft skills", value=resume.get("skills", ""), height=100, key="skills_input")

    st.divider()

    st.subheader("Certifications")
    st.text_area("Add relevant certifications or courses completed", value=resume.get("certifications", ""), height=100, key="certifications_input")

    # Submit button
    st.markdown("<div style='text-align:center; margin-top:30px;'>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Improve Sections")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Generate Suggestions ---
if submitted:
    with st.spinner("Improving your resume..."):
        resume["name"] = st.session_state.name_input
        resume["email"] = st.session_state.email_input
        resume["education"] = query_deepseek(f"Improve this education section:\n{st.session_state.education_input}")
        resume["experience"] = query_deepseek(f"Improve this experience section:\n{st.session_state.experience_input}")
        resume["projects"] = query_deepseek(f"Improve this projects section:\n{st.session_state.projects_input}")
        resume["skills"] = query_deepseek(f"Improve this skills section:\n{st.session_state.skills_input}")
        resume["certifications"] = query_deepseek(f"Improve this certifications section:\n{st.session_state.certifications_input}")
        st.success("Resume sections updated successfully!")

# --- Save updated data ---
st.session_state.resume_data.update(resume)
