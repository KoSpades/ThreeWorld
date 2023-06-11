from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Character(Base):
    __tablename__ = "characters"

    char_id = Column(Integer, primary_key=True, index=True)
    char_name = Column(String)
    element = Column(Integer, ForeignKey('elements.e_id', ondelete='CASCADE'))
    position = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    speed = Column(Integer)
