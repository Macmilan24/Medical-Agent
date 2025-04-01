# Medical AI Agent

Welcome to the Medical AI Agent project! This is a learning-focused initiative to create an AI-powered chatbot that answers basic medical questions using Groq's "llama-3.3-70b-versatile" model. Starting simple, this project aims to grow into a sophisticated medical assistant with advanced features like Retrieval-Augmented Generation (RAG), knowledge graphs, and multi-agent collaboration.

## Project Overview

This repository contains the initial version (Phase 1) of a Medical AI Agent—a command-line chatbot that connects to Groq's free LLM API to provide responses to medical queries (e.g., "What causes a headache?"). It’s built with Python and designed for educational purposes, offering a stepping stone to explore AI agent development in healthcare.

### Goals

- **Phase 1 (Current):** Build a basic chatbot with Groq's API.
- **Future Phases:** Add RAG for document retrieval, a knowledge graph for medical relationships, and multiple agents for complex tasks.

### Why This Project?

- Learn the basics of AI agent design and LLM integration.
- Explore practical applications of AI in medicine.
- Start simple and scale up with hands-on experience.

**Note:** This is not a diagnostic tool—always consult a healthcare professional for medical advice!

## Features

- Command-line interface for asking medical questions.
- Powered by Groq's "llama-3.3-70b-versatile" model via API.
- Simple, modular structure for easy expansion.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- A Groq API key (sign up at [Groq's website](https://groq.com))
- Basic familiarity with Python and terminal usage

### Setup Instructions

1. **Clone the Repository**

   - Run `git clone https://github.com/Ma/medical-ai-agent.git`
   - Navigate to the project folder: `cd medical-ai-agent`

2. **Set Up Virtual Environment**

   - Create: `python -m venv venv`
   - Activate:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**

   - Run `pip install -r requirements.txt`

4. **Configure API Key**

   - Create a `.env` file in the root folder.
   - Add: `GROQ_API_KEY=your_api_key_here`

5. **Run the Chatbot**
   - Start the agent: `python src/main.py`
   - Type a medical question and see the response!

For detailed setup steps, see [docs/setup.md](docs/setup.md).
