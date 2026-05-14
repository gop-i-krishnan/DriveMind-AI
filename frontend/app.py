import streamlit as st
import requests

st.set_page_config(
    page_title="TailorTalk AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 TailorTalk AI Drive Assistant")

st.markdown(
    "Search and discover files from Google Drive using AI."
)

# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input

user_input = st.chat_input(
    "Ask something about your files..."
)

if user_input:

    # Show user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response

    with st.chat_message("assistant"):

        with st.spinner("Searching Google Drive..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "message": user_input
                    }
                )

                data = response.json()

                ai_response = data["response"]

                st.code(ai_response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except Exception as e:

                error_message = f"Error: {str(e)}"

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )