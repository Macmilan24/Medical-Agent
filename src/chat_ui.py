import streamlit as st
import requests
import os
import uuid
import subprocess
import time
import atexit
from dotenv import load_dotenv

load_dotenv()

# Start the backend process if it isn't already running...
if "backend_process" not in st.session_state:
    backend_command = [
        "uvicorn",
        "src.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
    ]
    st.session_state.backend_process = subprocess.Popen(backend_command)
    time.sleep(3)


def stop_backend():
    if "backend_process" in st.session_state:
        st.session_state.backend_process.terminate()
        st.session_state.backend_process.wait()
        print("Backend server stopped.")


atexit.register(stop_backend)

# Initialize session state for chat history and session ID
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Custom CSS for chat bubbles and for fixed input form styling
chat_css = """
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
    padding: 10px;
    margin-bottom: 120px;  /* extra bottom margin to avoid overlap with fixed input */
}
.chat-bubble {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    max-width: 70%;
    display: inline-block;
}
.user-bubble {
    background-color: green ;
    text-align: right;
    padding: 10px;
    border-radius: 10px;
    float: right;
}
.assistant-bubble {
    text-align: left;
    float: left;
    clear: both;
}
.clearfix::after {
    content: "";
    clear: both;
    display: table;
}
/* Fixed input container styling */
#chat_input_container {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    padding: 10px;
    box-shadow: 0px -2px 5px rgba(0,0,0,0.1);
    z-index: 100;
}
</style>
"""
st.markdown(chat_css, unsafe_allow_html=True)

st.title("💬 Medical AI Chatbot")
st.write("Ask me any medical question, and I'll provide evidence-based answers.")

# Render the chat history in a container
chat_container = st.container()
with chat_container:
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            st.markdown(
                f"""
                <div class="clearfix">
                    <div class="user-bubble">
                        <strong>User:</strong> {chat['user']}
                    </div>
                    <div class="assistant-bubble">
                        <strong>Assistant:</strong> <br> {chat['assistant']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.write("No chat history yet. Start by asking a question!")

# Fixed container for the input form
st.markdown('<div id="chat_input_container">', unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "",
        key="user_input",
        label_visibility="collapsed",
        placeholder="Type your message here...",
    )
    submitted = st.form_submit_button("Send")
    if submitted:
        if user_input.strip():
            response = requests.post(
                os.environ.get("BACKEND_URL"),
                json={
                    "user_input": user_input,
                    "session_id": st.session_state.session_id,
                },
            )
            if response.status_code == 200:
                assistant_response = response.json().get("assistance")
                st.session_state.chat_history.append(
                    {"user": user_input, "assistant": assistant_response}
                )
                st.rerun()
            else:
                st.error("Error: Unable to get a response from the chatbot.")
        else:
            st.warning("Please enter a message.")
st.markdown("</div>", unsafe_allow_html=True)
