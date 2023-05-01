from pydantic import BaseModel


class ChatUserMessage(BaseModel):
    session_id: str
    content: str
