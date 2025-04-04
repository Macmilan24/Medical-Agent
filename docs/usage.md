# Using the Medical AI Agent

This is a web-based chatbot using RAG with Pinecone and Groq’s `llama-3.3-70b-versatile` to answer medical questions with data-backed responses.

## Overview

The agent retrieves medical info from Pinecone’s `medical-rag` index and enhances Groq’s answers. It’s for educational use—consult a doctor for real advice.

## Starting the Chatbot

- Follow `setup.md` to run the server.
- Confirm it’s live at `http://127.0.0.1:8000` (browser shows FastAPI page).
- On first run, it auto-populates Pinecone with PDFs from `data/` if empty.

## Interacting with the Chatbot

- Send a POST request to `/chat`:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"user_input": "What’s the treatment for hypertension?"}' \
       http://127.0.0.1:8000/chat
  ```

  **Response:**

  ```json
  { "assistance": "Treatment includes lifestyle changes… [from dataset]" }
  ```

- Answers use data from Pinecone for accuracy.

### Example Questions

- "What causes diabetes?"
- "How do I treat a minor burn?"
- "What’s the treatment for hypertension?"

### Limitations

- Depends on PDFs in `data/` — out-of-scope questions use Groq’s general knowledge.
- To add more data, update `data/` and restart the server (it’ll upload if index is empty).

## Stopping the Chatbot

- Press `Ctrl+C` in the terminal.

---

Enjoy your data-driven medical assistant!
