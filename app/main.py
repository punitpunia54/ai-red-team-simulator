from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def home():
    return {"message": "AI Red Team Simulator Running"}