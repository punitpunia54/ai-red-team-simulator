from pydantic import BaseModel


class AttackRequest(BaseModel):
    company_type: str
    attack_type: str


class AttackResponse(BaseModel):
    summary: str
    risk_level: str
    attack_chain: list[str]