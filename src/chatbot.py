from src.llm_api import get_groq_response
from src.rag import get_data_from_pinecone
from typing import List, Tuple

converstion_history: List[Tuple[str, str]] = []


def get_chat_reponse(user_input: str) -> str:
    """
    Accepts user input and gets the response from Groq API.
    Args:
        user_input (str): User input.

    Returns:
        str: Response from Groq API.
    """

    global converstion_history
    context, source = get_data_from_pinecone(user_input)

    memeory_context = "\n\n".join(
        [f"User: {q}\nAssistant: {a}" for q, a in converstion_history]
    )

    query = f"Conversation history:\n\n{memeory_context}\n\n" if memeory_context else ""
    query += f"Based on this info (From RAG):\n\n{context}\n\n Answer: {user_input}\n\n"
    if context and source:
        query += f"Use the source from here:\n\n{source}\n\n"
    query += "Answer in a concise and informative manner. If the answer is not available, say 'I don't know'."

    response = get_groq_response(query)

    converstion_history.append((user_input, response))

    return response
