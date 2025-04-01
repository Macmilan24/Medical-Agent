# Using the Medical AI Agent

This guide shows how to use the Medical AI Agent, a web-based chatbot that answers medical questions using Groq’s `llama-3.3-70b-versatile` model.

## Overview

The agent runs as a FastAPI server and responds to medical queries via the `/chat` endpoint. It’s for **educational purposes**—always consult a doctor for real medical advice.

## Starting the Chatbot

1. Follow `setup.md` to set up and run the server.
2. Confirm it’s live by visiting `http://127.0.0.1:8000` in a browser (you’ll see FastAPI’s default page).

## Interacting with the Chatbot

- Send a **POST** request to `http://127.0.0.1:8000/chat` with JSON in this format:

  ```json
  {
    "user_input": "Your question here"
  }
  ```

- Example using **curl**:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"user_input": "What’s a fever?"}' \
  http://127.0.0.1:8000/chat
  ```

- **Response:** You’ll get JSON like:

  ```json
  {
    "assistance": "A fever is a temporary increase in body temperature, often due to illness."
  }
  ```

### **Alternative:** Use Postman or a similar tool to send the POST request.

## Example Questions

- “What causes a headache?”
- “How do I treat a minor burn?”
- “Why do I feel tired?”

## Stopping the Chatbot

Press `Ctrl+C` in the terminal to stop the server.
