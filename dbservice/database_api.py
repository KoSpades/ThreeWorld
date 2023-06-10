from .database import engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

from .crud import (element_repo, element_relation_repo,)
from contextlib import contextmanager

# global engine

def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')

@contextmanager
def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    event.listen(engine, 'connect', _fk_pragma_on_connect)
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_element(e_id, e_name):
    with get_db() as session:
        res = element_repo.create_element(session, e_id, e_name)
        return res

def remove_all_elements():
    with get_db() as session:
        element_repo.remove_all_elements(session)

def create_element_relation(attack_e_id, defense_e_id, multiplier):
    with get_db() as session:
        res = element_relation_repo.create_element_relation(session, attack_e_id, defense_e_id, multiplier)
        return res

def remove_all_element_relations():
    with get_db() as session:
        element_relation_repo.remove_all_element_relations(session)
