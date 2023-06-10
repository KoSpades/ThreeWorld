from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# on disk global engine
DATABASE_URL = "sqlite:///./three_world.db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

