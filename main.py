import streamlit as st

st.set_page_config(page_title="AI Resume Builder", layout="centered")

# Load styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>AI Resume Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Create, enhance, and optimize your resume with intelligent suggestions and job description analysis.</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>Resume Builder</h3>
        <p>Use the left sidebar and click 'Resume Builder' to begin entering and improving your resume step by step.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>Job Match Analysis</h3>
        <p>Use the left sidebar and click 'ATS Matcher' to check how well your resume aligns with any job description.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 14px;'>Use the sidebar on the left to navigate between sections.</p>", unsafe_allow_html=True)
