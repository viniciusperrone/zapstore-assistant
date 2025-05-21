from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ping():
    return {"msg": "ZapStore Bot is running!"}
