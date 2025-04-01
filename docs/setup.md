# Setup Guide for Medical AI Agent

This guide explains how to set up the Medical AI Agent, a web-based chatbot powered by Groq’s `llama-3.3-70b-versatile` model.

## Prerequisites

- Python 3.12 (download from [python.org](https://www.python.org/downloads/))
- A code editor (e.g., VSCode)
- Terminal or command-line access
- (Optional) Git for cloning the project

## Get the Project

- Download and unzip the `medical_ai_agent` folder, or clone it with:

  ```bash
  git clone <repository-url>
  ```

## Set Up the Environment

1. Open your terminal and navigate to the project folder:

   ```bash
   cd medical_ai_agent
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it:

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
     You’ll see `(venv)` in your prompt.

## Install Dependencies

- Install required libraries:

  ```bash
  pip install -r requirements.txt
  ```

## Get a Groq API Key

1. Sign up at [Groq](https://groq.com).
2. Go to the developer section and generate an API key.
3. Create a `.env` file in the project root:

   ```bash
   echo "GROQ_API_KEY=your_key_here" > .env
   ```

   **Note:** Keep your API key secret—don’t share `.env`!

## Run the Chatbot

- Start the FastAPI server:

  ```bash
  uvicorn src.main:app --reload
  ```

- Check it’s running at [http://127.0.0.1:8000](http://127.0.0.1:8000) (open in a browser to see FastAPI’s default page).
