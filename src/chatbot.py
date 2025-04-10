from src.llm_api import get_groq_response
from src.rag import get_data_from_pinecone
from typing import List, Tuple

# Memory to store conversation history
conversation_memory: List[Tuple[str, str]] = []


def get_chat_reponse(user_input: str) -> str:
    """
    Accepts user input and gets the response from Groq API, with context awareness.
    Args:
        user_input (str): User input.

    Returns:
        str: Response from Groq API.
    """
    global conversation_memory

    # Retrieve context and source from Pinecone
    context, source = get_data_from_pinecone(user_input)

    # Build the query with memory
    memory_context = "\n\n".join(
        [f"User: {q}\nAssistant: {a}" for q, a in conversation_memory[-5:]]
    )
    query = f"Conversation so far:\n\n{memory_context}\n\n" if memory_context else ""
    query += f"Based on this info:\n\n{context}\n\nAnswer: {user_input}\n\n"

    if context and source:
        query += f"Use the source from here:\n\n{source}\n\n"
    query += "Answer in a concise and informative manner. If the answer is not available, say 'I don't know'."

    if len(context) < 100 and not memory_context:
        query = f"I don't know based on the available information, but here is my thought:\n\n{user_input}\n\n"

    # Get response from Groq API
    try:
        response = get_groq_response(query)
    except Exception as e:
        print(f"Error in get_chat_reponse: {e}")
        return "I'm sorry, something went wrong. Please try again later."

    # Update memory with the latest interaction
    conversation_memory.append((user_input, response))

    return response
