from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Ability(Base):
    __tablename__ = "abilities"

    a_id = Column(Integer, primary_key=True, index=True)
    a_name = Column(String)
    power = Column(Integer)
    element = Column(Integer, ForeignKey('elements.e_id', ondelete='CASCADE'))
    target_type = Column(String)
    starting_pp = Column(Integer)
    consuming_pp = Column(Integer)
