# Using the Medical AI Agent

This is a context-aware chatbot with a Streamlit UI, using RAG with Pinecone and Groq’s "llama-3.3-70b-versatile" to answer medical questions with data-backed responses.

## Overview

The agent retrieves medical info from Pinecone’s `medical-rag` index, remembers the last 5 exchanges per session, and enhances Groq’s answers. It’s for educational use—consult a doctor for real advice.

## Starting the Chatbot

- Follow `setup.md` to run the UI.
- Open [http://localhost:8501](http://localhost:8501) in your browser.
- On first run, the backend auto-populates Pinecone with PDFs from `data/` if empty.

## Interacting with the Chatbot

### Via UI

- Type your question in the fixed input box at the bottom.
- Hit “Send” to see the response displayed as chat bubbles.
- Follow up with additional questions (e.g., “Explain more”)—it remembers the last 5 exchanges per session!

### Via API (Advanced)

Send a POST request:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"user_input": "What’s hypertension?", "session_id": "your_id"}' \
     http://127.0.0.1:8000/chat
```

**Response:**

```json
{ "assistance": "Hypertension is… [from dataset]" }
```

#### Example Conversation

- **You:** “What is a protein-coding gene?”
- **Agent:** “It’s a gene that codes for proteins…”
- **You:** “Would you explain it more?”
- **Agent:** “Building on that, it involves transcription and translation…”

## Limitations

- Depends on PDFs in `data/`—out-of-scope questions use Groq’s general knowledge.
- Memory resets when the UI restarts—only the last 5 exchanges per session are remembered.
- To add more data, update the contents of the `data/` folder and restart the UI.

## Stopping the Chatbot

- Close the browser or press `Ctrl+C` in the terminal (which stops the UI and backend).

Enjoy your conversational medical assistant!
