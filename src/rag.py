from src.upload_to_pinecone import query_pinecone
from src.embedding import get_embeddings


def get_data_from_pinecone(query: str):
    """
    Query Pinecone index for similar vectors based on the provided query.

    Args:
        query (str): The query string to search for.

    Returns:
        Tuple[str, str]: A tuple containing the context and source.
    """
    query_vector = get_embeddings(query)
    pinecone_response = query_pinecone(query_vector)

    context = []
    source = []

    if len(pinecone_response) > 0:
        for i in range(min(3, len(pinecone_response))):
            context.append(pinecone_response[i]["metadata"]["text"])
            source.append(pinecone_response[i]["metadata"]["source"])

    # Join lists into strings
    return "\n\n".join(context), "\n".join(source)
