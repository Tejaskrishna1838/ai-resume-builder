import streamlit as st
import requests

# ✅ Your new DeepSeek API key (DO NOT SHARE PUBLICLY)
API_KEY = "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"
MODEL_ID = "deepseek/deepseek-chat-v3-0324:free"

# ✅ Query DeepSeek with safe fallback if error occurs
def query_deepseek(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"❌ API Error: {data['error'].get('message', 'Unknown error')}"
        else:
            return "❌ Unexpected response from API."
    except Exception as e:
        return f"❌ Exception occurred: {e}"

# ✅ Initialize resume input memory for Streamlit session
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
