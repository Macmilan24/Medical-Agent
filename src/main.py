import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.chatbot import get_chat_reponse
from src.upload_to_pinecone import upload_to_pinecone
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index_name = "medical-rag"
index = pc.Index(index_name)


@asynccontextmanager
async def lifespan(app: FastAPI):
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
        print(f"Index {index_name} created.")
    else:
        print(f"Index {index_name} already exists.")

    stats = index.describe_index_stats()
    vector_count = stats.get("total_vector_count", 0)

    if vector_count == 0:
        print("Index is empty. Populating with data from 'data/' folder...")
        upload_to_pinecone(data_folder="data", max_pages=300, batch_size=50)
        print("Index population complete.")
    else:
        print(f"Index already has {vector_count} vectors. Skipping upload.")

    yield


app = FastAPI(lifespan=lifespan)


class Chat_Request(BaseModel):
    user_input: str


@app.post("/chat")
async def chat_with_ai(request: Chat_Request):
    try:
        response = get_chat_reponse(request.user_input)
        return {"assistance": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
