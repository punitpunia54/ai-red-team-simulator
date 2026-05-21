from fastapi import APIRouter
from app.schemas.attack import AttackRequest
from app.services.ai_service import generate_attack_simulation

router = APIRouter()


@router.post("/simulate")
async def simulate_attack(data: AttackRequest):

    result = await generate_attack_simulation(
        data.company_type,
        data.attack_type
    )

    return result