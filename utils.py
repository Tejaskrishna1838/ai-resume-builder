import streamlit as st
import requests

# Your DeepSeek API key from OpenRouter
API_KEY = "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"  # replace with your real key
MODEL_ID = "deepseek/deepseek-chat-v3-0324:free"

# AI Suggestion Function with Error Handling
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

        # ✅ Handle missing 'choices' key or API error
        if 'choices' in data:
            return data['choices'][0]['message']['content']
        elif 'error' in data:
            return f"❌ API Error: {data['error'].get('message', 'Unknown error')}"
        else:
            return "❌ Unexpected API response. Please verify your API key or prompt."
    except Exception as e:
        return f"❌ Exception occurred: {e}"

# Initialize session state for resume data
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

