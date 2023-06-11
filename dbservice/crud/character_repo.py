from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.character import Character

def create_character(db: Session, char_id, char_name, element, position, hp, attack, defense, speed):
    db_character = Character(char_id=char_id,
                             char_name=char_name,
                             element=element,
                             position=position,
                             hp=hp,
                             attack=attack,
                             defense=defense,
                             speed=speed,)
    try:
        db.add(db_character)
        db.commit()
        db.refresh(db_character)
    except SQLAlchemyError as e:
        db.rollback()
        return 1
    return 0

def remove_all_characters(db: Session):
    db.query(Character).delete()
    db.commit()
