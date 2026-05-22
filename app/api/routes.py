from fastapi import APIRouter
from app.schemas.attack import AttackRequest
from app.services.ai_service import generate_attack_simulation

from app.core.database import SessionLocal
from app.models.attack import AttackSimulation

router = APIRouter()


@router.post("/simulate")
async def simulate_attack(data: AttackRequest):

    db = SessionLocal()

    result = await generate_attack_simulation(
        data.company_type,
        data.attack_type
    )

    # Save to database
    
    attack = AttackSimulation(
        company_type=data.company_type,
        attack_type=data.attack_type,
        summary=result["summary"],
        risk_level=result["risk_level"]
    )

    db.add(attack)
    db.commit()

    return result

@router.get("/simulations")
async def get_simulations():

    db = SessionLocal()

    simulations = db.query(AttackSimulation).all()

    return simulations