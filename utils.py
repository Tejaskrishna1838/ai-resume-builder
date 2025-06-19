import streamlit as st
import requests

# ✅ Securely load your OpenRouter API key from Streamlit secrets
API_KEY = st.secrets["API_KEY"]
MODEL_ID = "deepseek/deepseek-chat-v3-0324:free"

# ✅ Function to query DeepSeek API with prompt
def query_deepseek(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_ID,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()

        if response.status_code == 200 and "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"❌ API Error: {data['error'].get('message', 'Unknown error')}"
        else:
            return f"❌ Unexpected API Response: {response.text}"
    except Exception as e:
        return f"❌ Exception: {e}"

# ✅ Session state initialization for resume form
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

