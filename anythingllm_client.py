import requests
import streamlit as st


def query_anythingllm(message: str):
    BASE_URL = st.secrets["ANYTHINGLLM_BASE_URL"]
    API_KEY = st.secrets["ANYTHINGLLM_API_KEY"]
    SLUG = st.secrets["ANYTHINGLLM_WORKSPACE_SLUG"]  # ✅ FIXED

    url = f"{BASE_URL}/api/v1/workspaces/{SLUG}/chat"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "message": message
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        # 🔍 Show errors clearly
        if response.status_code != 200:
            return f"❌ Error {response.status_code}: {response.text}"

        data = response.json()

        # ✅ Handle different response formats
        return (
            data.get("text")
            or data.get("response")
            or data.get("output")
            or str(data)
        )

    except Exception as e:
        return f"🚨 Request failed: {str(e)}"
