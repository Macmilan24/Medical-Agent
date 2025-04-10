import os
from pinecone import Pinecone
from dotenv import load_dotenv
from src.embedding import generate_embeddings
from src.data_processing import process_documents
from typing import List

load_dotenv()

# Assume that the index is created in main.py.
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index_name = "medical-rag"
index = pc.Index(index_name)


def batch(iterable, batch_size=100):
    """
    Helper function to split an iterable into smaller batches.
    """
    for i in range(0, len(iterable), batch_size):
        yield iterable[i : i + batch_size]


def upload_to_pinecone(data_folder: str, max_pages: int = 100, batch_size: int = 50):
    """
    Process documents, generate embeddings, and upload them to Pinecone in batches.

    Args:
        data_folder (str): The folder containing PDF files.
        max_pages (int, optional): The maximum number of pages to process per PDF. Defaults to 100.
        batch_size (int, optional): The number of vectors to upload in each batch. Defaults to 50.
    """
    print("Processing documents...")
    processed_data = process_documents(data_folder, max_pages=max_pages)

    print("Generating embeddings...")
    embeddings = generate_embeddings(processed_data)

    print("Preparing vectors for Pinecone...")
    pinecone_vectors = [
        {
            "id": item["chunk_id"],
            "values": item["embedding"],
            "metadata": {
                "source": item["source"],
                "text": item["text"],
            },
        }
        for item in embeddings
    ]

    print(
        f"Uploading {len(pinecone_vectors)} vectors to Pinecone in batches of {batch_size}..."
    )
    for vector_batch in batch(pinecone_vectors, batch_size):
        index.upsert(vectors=vector_batch)
    print("Upload Complete!")


def query_pinecone(query_embedding: List, top_k: int = 3, metadata: bool = True):
    """
    Query Pinecone index for similar vectors.

    Args:
        query_embedding (List): The embedding of the query text.
        top_k (int, optional): The number of similar vectors to return. Defaults to 3.
        metadata (bool, optional): Whether to include metadata in the response. Defaults to True.

    Returns:
        List: A list of similar vectors from the Pinecone index.
    """
    try:
        query_response = index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=metadata,
        )
        return query_response["matches"]
    except Exception as e:
        print(f"Error querying Pinecone: {e}")  # Log the error
        return []
