import streamlit as st
import requests

# OpenRouter DeepSeek API Key
API_KEY = "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"
MODEL_ID = "deepseek/deepseek-chat-v3-0324:free"

# AI Suggestion Function
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
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"[Error] {e}"

# Initialize Resume Data in Session
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
