import requests
import streamlit as st


def query_anythingllm(message: str):
    BASE_URL = st.secrets["ANYTHINGLLM_BASE_URL"]
    API_KEY = st.secrets["ANYTHINGLLM_API_KEY"]
    SLUG = st.secrets["WORKSPACE_SLUG"]

    url = f"{BASE_URL}/api/v1/workspaces/{SLUG}/chat"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "message": message
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text
