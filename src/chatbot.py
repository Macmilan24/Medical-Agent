from src.llm_api import get_groq_response
from src.rag import get_data_from_pinecone


def get_chat_reponse(user_input: str) -> str:
    """
    Accepts user input and gets the response from Groq API.
    Args:
        user_input (str): User input.

    Returns:
        str: Response from Groq API.
    """
    context, source = get_data_from_pinecone(user_input)

    query = f"Based on this info:\n\n{context}\n\n Answer: {user_input}\n\n"
    if context and source:
        query += f"Use the source from here:\n\n{source}\n\n"
    query += "Answer in a concise and informative manner. If the answer is not available, say 'I don't know'."

    if len(context) < 100:
        query = f" say I don't know based on the available information, but here is my thought:\n\n{user_input}\n\n"

    return get_groq_response(query)
