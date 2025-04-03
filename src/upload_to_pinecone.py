import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from embedding import generate_embeddings
from data_processing import process_documents

load_dotenv()

pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY"),
)

index_name = "medical-rag"
if index_name not in pc.list_indexes().names():
    print(f"Creating index {index_name} ...")
    pc.create_index(
        name=index_name,
        dimension=384,
        spec=ServerlessSpec(
            cloud="aws",
            region=os.environ.get("PINECONE_REGION"),
        ),
    )
else:
    print(f"Index {index_name} already exists.")
    print(f"Connecting to index {index_name} ...")
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


if __name__ == "__main__":
    data_folder = "data"
    upload_to_pinecone(data_folder, max_pages=300, batch_size=50)
