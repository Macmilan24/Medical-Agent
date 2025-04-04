# Setup Guide for Medical AI Agent

This guide sets up the Medical AI Agent, a RAG-enabled chatbot using Groq and Pinecone.

## Prerequisites

- Python 3.12 ([Download](https://www.python.org/downloads/))
- A code editor (e.g., VSCode)
- Terminal access
- Accounts: Groq, Pinecone

## Get the Project

Clone or download this repository:

```bash
git clone <repository-url>
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

Includes `fastapi`, `uvicorn`, `pinecone-client`, `sentence-transformers`, `pdfplumber`, etc.

## Configure API Keys

### Groq API Key

- Sign up at [groq.com](https://groq.com), get an API key.
- Add it to the `.env` file:

```bash
echo "GROQ_API_KEY=your_key" >> .env
```

### Pinecone API Key

- Sign up at [pinecone.io](https://www.pinecone.io), get an API key and region (e.g., `us-west1-gcp`).
- Add it to the `.env` file:

```bash
echo "PINECONE_API_KEY=your_key" >> .env
echo "PINECONE_REGION=your_region" >> .env
```

## Prepare Medical Data

- Add medical PDFs to the `data/` folder (e.g., public health guides, 5–10 files to start).
- On first run, the chatbot automatically creates the `medical-rag` Pinecone index and uploads this data if the index is empty.

## Run the Chatbot

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Check it’s running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

On startup, it’ll create/populate the Pinecone index if needed—watch the logs!
