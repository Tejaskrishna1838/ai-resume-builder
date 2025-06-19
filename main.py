import streamlit as st
import requests

# ✅ DEBUG: Check if API key is available in secrets
st.sidebar.write("✅ API Key Loaded" if "API_KEY" in st.secrets else "❌ API Key Missing")

st.set_page_config(page_title="AI Resume Builder", layout="centered")

# Load custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>AI Resume Builder</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Create, enhance, and optimize your resume with AI-powered suggestions and ATS feedback.</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>Build Resume</h3>
        <p>Use the left sidebar and click 'Resume Builder' to begin building your resume with AI suggestions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>ATS Match</h3>
        <p>Use the left sidebar and click 'ATS Matcher' to check how well your resume matches a job description.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 14px;'>Use the sidebar on the left to navigate between pages.</p>", unsafe_allow_html=True)
