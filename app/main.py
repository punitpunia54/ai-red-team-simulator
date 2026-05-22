from fastapi import FastAPI
from app.api.routes import router

from app.core.database import engine
from app.models.attack import AttackSimulation

# Create the database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router)


@app.get("/")
async def home():
    return {"message": "AI Red Team Simulator Running"}