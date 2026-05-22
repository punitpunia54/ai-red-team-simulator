from sqlalchemy import Column, Integer, String
from app.core.database import Base


class AttackSimulation(Base):

    __tablename__ = "attack_simulations"

    id = Column(Integer, primary_key=True, index=True)

    company_type = Column(String)
    attack_type = Column(String)

    summary = Column(String)
    risk_level = Column(String)