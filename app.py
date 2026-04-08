 import requests
import streamlit as st
from anythingllm_client import query_anythingllm


def main():
        st.set_page_config(page_title="UniGuide AI", layout="wide")

    page = st.sidebar.radio("Navigation", ["Home", "Chat", "About"])

    st.title("🎓 UniGuide AI")
    st.write("Your smart assistant for universities in Jamaica 🇯🇲")

    # ---------------- HOME ----------------
    if page == "Home":
        st.header("Welcome to UniGuide AI")
        st.write(
            """
            This AI helps students:
            - Find universities in Jamaica
            - Understand entry requirements
            - Explore programs
            - Compare tuition
            """
        )

    # ---------------- CHAT ----------------
    elif page == "Chat":
        st.header("💬 Ask UniGuide AI")

        user_input = st.text_input("Enter your question:")

        if st.button("Submit"):
            if user_input.strip():
                with st.spinner("Thinking..."):
                    answer = query_anythingllm(user_input)

                st.success(f"**UniGuide AI:** {answer}")
            else:
                st.warning("Please enter a question.")

    # ---------------- ABOUT ----------------
    elif page == "About":
        st.header("About UniGuide AI")
        st.write(
            """
            UniGuide AI is designed to help students make informed decisions
            about universities in Jamaica using AI.
            """
        )

    else:
        st.error("Unknown page selected.")


if __name__ == "__main__":
    main()
