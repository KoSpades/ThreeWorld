from sqlalchemy import Column, Integer, Float, ForeignKey
from ..database import Base

class ElementRelation(Base):
    __tablename__ = "element_relations"

    attack_e_id = Column(Integer, ForeignKey('elements.e_id'), primary_key=True)
    defense_e_id = Column(Integer, ForeignKey('elements.e_id'), primary_key=True)
    multiplier = Column(Float)
