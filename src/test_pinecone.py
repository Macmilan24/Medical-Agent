import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(os.environ.get("PINECONE_API_KEY"))

try:
    index = pc.Index("medical-rag")

    metadata = index.describe_index_stats()
    print("Pinecone connected")
    print(metadata)
except Exception as e:
    print(e)
    print("Failed to Connect to Pincone")
