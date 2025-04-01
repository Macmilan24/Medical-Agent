from llm_api import get_groq_response


def get_chat_reponse(user_input: str) -> str:
    """
    Accepts user input and get the response from Groq API

    Args:
        user_input (str): user input


    Returns:
        str: Response from Groq API
    """
    return get_groq_response(user_input)
