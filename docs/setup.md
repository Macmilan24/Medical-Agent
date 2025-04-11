# Setup Guide for Medical AI Agent

This guide sets up the Medical AI Agent, a RAG-enabled, context-aware chatbot using Groq, Pinecone, and a Streamlit UI.

## Prerequisites

- Python 3.12 (available from [python.org](https://www.python.org/downloads/))
- A code editor (e.g., VSCode)
- Terminal access
- Accounts for Groq and Pinecone

## Get the Project

Clone or download the repository:

```bash
git clone https://github.com/Macmilan24/Medical-Agent.git
cd medical_ai_agent
```

## Set Up the Environment

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

_This installs packages such as `fastapi`, `uvicorn`, `pinecone-client`, `sentence-transformers`, `pdfplumber`, and `streamlit`._

## Configure API Keys

### Groq API Key

1. Sign up at [groq.com](https://groq.com) and obtain an API key.
2. Add it to the `.env` file:
   ```bash
   echo "GROQ_API_KEY=your_key" >> .env
   ```

### Pinecone API Key

1. Sign up at [pinecone.io](https://www.pinecone.io) and get an API key along with your region (e.g., `us-west1-gcp`).
2. Add the API key and region to the `.env` file:
   ```bash
   echo "PINECONE_API_KEY=your_key" >> .env
   echo "PINECONE_REGION=your_region" >> .env
   ```

### Backend URL

Add the backend URL to the `.env` file:

```bash
echo "BACKEND_URL=http://127.0.0.1:8000/chat" >> .env
```

## Prepare Medical Data

Add medical PDFs to the `data/` folder (e.g., public health guides, 5–10 files to start).  
On the first run, the backend auto-creates the `medical-rag` Pinecone index and uploads the data if the index is empty.

## Run the Chatbot

Start the Streamlit UI (this will automatically launch the FastAPI backend):

```bash
streamlit run src/chat_ui.py
```

Open your browser to [http://localhost:8501](http://localhost:8501) (Streamlit's default URL).  
On startup, the backend will populate Pinecone if needed—watch the terminal logs for details!
