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


# not the main usage but just to Practice

# user_input = ""
# print("Welcome to MediAI! How can I assist you today?")
# while user_input != "No":
#     user_input = input("You: ")
#     result = get_chat_reponse(user_input)
#     print("MediAI: " + result + "\n\n\n\n")

#     print("Do you want to continue? (Yes/No)")
#     user_input = input("You: ")
