import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Medical AI Chatbot")
st.write("Ask me any medical question, and I'll provide evidence-based answers.")

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**User:** {chat['user']}")
    st.markdown(f"**Assistant:** \n {chat['assistant']}")

# Input box for user query
user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input.strip():
        # Send the user input to the FastAPI backend
        response = requests.post(
            os.environ.get("BACKEND_URL"), json={"user_input": user_input}
        )
        if response.status_code == 200:
            assistant_response = response.json().get("assistance")
            # Update chat history
            st.session_state.chat_history.append(
                {"user": user_input, "assistant": assistant_response}
            )
            # Display the new chat
            st.markdown(f"**User:** {user_input}")
            st.markdown(f"**Assistant:** {assistant_response}")
        else:
            st.error("Error: Unable to get a response from the chatbot.")
    else:
        st.warning("Please enter a question.")
