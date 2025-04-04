from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.chatbot import get_chat_reponse


class Chat_Request(BaseModel):
    user_input: str


app = FastAPI()


@app.post("/chat")
async def chat_with_ai(request: Chat_Request):
    try:
        response = get_chat_reponse(request.user_input)
        return {"assitance": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
