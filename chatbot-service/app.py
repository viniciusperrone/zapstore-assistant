from fastapi import FastAPI, Request
from models.message import Message


app = FastAPI()

@app.post("/chatbot/assistant")
async def root(request: Request):
    print(request.json())

    return {'status': 'ok'}

