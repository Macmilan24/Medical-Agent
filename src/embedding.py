from sentence_transformers import SentenceTransformer
from typing import List, Dict

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(processed_data: List[str]) -> List[Dict[str, any]]:
    """
    Generate embeddings for a list of text chunks.

    Args:
        processed_data (List[str]): A list of text chunks.

    Returns:
        List[Dict[str, any]]: A list of dictionaries containing the chunk ID, text, and its embedding.
    """

    chunks = [item["text"] for item in processed_data]
    sources = [item["source"] for item in processed_data]
    chunk_ids = [item["chunk_id"] for item in processed_data]

    embeddings = model.encode(chunks, convert_to_numpy=True)
    embeddings_list = []

    for i, chunk in enumerate(chunks):
        embeddings_list.append(
            {
                "chunk_id": chunk_ids[i],
                "text": chunk,
                "source": sources[i],
                "embedding": embeddings[i].tolist(),
            }
        )

    return embeddings_list


def get_embeddings(text: str) -> List[float]:
    """
    Generate embeddings for a single text chunk.

    Args:
        text (str): A text chunk.

    Returns:
        List[float]: The embedding of the text chunk.
    """
    return model.encode(text, convert_to_numpy=True).tolist()
