from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.element_relation import ElementRelation

def create_element_relation(db: Session, attack_e_id, defense_e_id, multiplier):
    db_element_relation = ElementRelation(attack_e_id=attack_e_id,
                                          defense_e_id=defense_e_id,
                                          multiplier=multiplier,)
    try:
        db.add(db_element_relation)
        db.commit()
        db.refresh(db_element_relation)
    except SQLAlchemyError as e:
        db.rollback()
        return 1
    return 0

def remove_all_element_relations(db: Session):
    db.query(ElementRelation).delete()
    db.commit()
