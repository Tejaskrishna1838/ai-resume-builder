import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load the Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Function to query Gemini
def query_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini Error: {e}"

# Initialize session state for resume data and ATS result
def init_session():
    if "resume_data" not in st.session_state:
        st.session_state.resume_data = {
            "name": "",
            "email": "",
            "education": "",
            "experience": "",
            "projects": "",
            "skills": "",
            "certifications": ""
        }

    if "job_description" not in st.session_state:
        st.session_state.job_description = ""

    if "ats_result" not in st.session_state:
        st.session_state.ats_result = ""
