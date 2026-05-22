from fastapi import FastAPI
from app.api.routes import router

from app.core.database import Base, engine
from app.models.attack import AttackSimulation

from fastapi.middleware.cors import CORSMiddleware
    

# Create the database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def home():
    return {"message": "AI Red Team Simulator Running"}