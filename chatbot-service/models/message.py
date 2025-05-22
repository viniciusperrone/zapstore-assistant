from pydantic import BaseModel


class Message(BaseModel):
    author: str
    message: str
