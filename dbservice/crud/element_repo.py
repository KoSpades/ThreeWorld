from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.element import Element

def create_element(db: Session, e_id, e_name):
    db_element = Element(e_id=e_id,
                         e_name=e_name,)
    try:
        db.add(db_element)
        db.commit()
        db.refresh(db_element)
    except SQLAlchemyError as e:
        db.rollback()
        return 1
    return 0

def remove_all_elements(db: Session):
    db.query(Element).delete()
    db.commit()
