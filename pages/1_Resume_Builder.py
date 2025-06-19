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
st.markdown("Fill in your resume sections below and click **Improve Sections** to enhance them.")

# --- Resume Form ---
with st.form("resume_form"):

    st.subheader("Personal Details")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value=resume.get("name", ""), key="name_input")
        with col2:
            st.text_input("Email", value=resume.get("email", ""), key="email_input")

    st.subheader("Education")
    st.text_area("Describe your education background", value=resume.get("education", ""), key="education_input")

    st.subheader("Experience")
    st.text_area("List your work or internship experience", value=resume.get("experience", ""), key="experience_input")

    st.subheader("Projects")
    st.text_area("Mention any projects you've worked on", value=resume.get("projects", ""), key="projects_input")

    st.subheader("Skills")
    st.text_area("List your technical and soft skills", value=resume.get("skills", ""), key="skills_input")

    st.subheader("Certifications")
    st.text_area("Mention any certifications", value=resume.get("certifications", ""), key="certifications_input")

    submitted = st.form_submit_button("Improve Sections")
    if submitted:
        with st.spinner("Generating AI suggestions..."):
            st.session_state.resume_data.update({
                "name": st.session_state.name_input,
                "email": st.session_state.email_input,
                "education": query_deepseek(f"Improve this education section:\n{st.session_state.education_input}"),
                "experience": query_deepseek(f"Improve this experience section:\n{st.session_state.experience_input}"),
                "projects": query_deepseek(f"Improve this projects section:\n{st.session_state.projects_input}"),
                "skills": query_deepseek(f"Improve this skills section:\n{st.session_state.skills_input}"),
                "certifications": query_deepseek(f"Improve this certifications section:\n{st.session_state.certifications_input}")
            })

        st.success("Sections enhanced successfully!")

        # Show updated sections
        st.markdown("---")
        st.subheader("Preview of Improved Sections")
        st.markdown(f"**Full Name:** {st.session_state.resume_data['name']}")
        st.markdown(f"**Email:** {st.session_state.resume_data['email']}")
        st.markdown("**Education:**")
        st.info(st.session_state.resume_data['education'])

        st.markdown("**Experience:**")
        st.info(st.session_state.resume_data['experience'])

        st.markdown("**Projects:**")
        st.info(st.session_state.resume_data['projects'])

        st.markdown("**Skills:**")
        st.info(st.session_state.resume_data['skills'])

        st.markdown("**Certifications:**")
        st.info(st.session_state.resume_data['certifications'])
