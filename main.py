import os
from dotenv import load_dotenv
from fastapi import FastAPI
import openai
from src.chat import Chat
from pydantic import BaseModel


class ChatUserMessage(BaseModel):
    message: str


load_dotenv()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_bot = Chat()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/list")
async def list_models():
    return {"result": openai.Model.list()}


@app.post("/chat")
def chat(m: ChatUserMessage):
    print(m)
    return chat_bot.ask_something(m.message)


if __name__ == "__main__":
    pass
