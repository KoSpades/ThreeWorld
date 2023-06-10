from sqlalchemy import Column, Integer, String
from ..database import Base

class Element(Base):
    __tablename__ = "elements"

    e_id = Column(Integer, primary_key=True, index=True)
    e_name = Column(String)
    