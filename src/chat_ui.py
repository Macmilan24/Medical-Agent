import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Medical AI Chatbot")
st.write("Ask me any medical question, and I'll provide evidence-based answers.")

# Input box for user query
user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input.strip():
        # Send the user input to the FastAPI backend
        response = requests.post(
            os.environ.get("BACKEND_URL"), json={"user_input": user_input}
        )
        if response.status_code == 200:
            st.markdown(f"**Assistant:** {response.json().get('assistance')}")
        else:
            st.error("Error: Unable to get a response from the chatbot.")
    else:
        st.warning("Please enter a question.")
