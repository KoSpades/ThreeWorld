from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..schemas.ability import Ability

def create_ability(db: Session, a_id, a_name, char_id, power, element, target_type, starting_pp, consuming_pp):
    db_ability = Ability(a_id=a_id,
                         a_name=a_name,
                         char_id=char_id,
                         power=power,
                         element=element,
                         target_type=target_type,
                         starting_pp=starting_pp,
                         consuming_pp=consuming_pp,)
    try:
        db.add(db_ability)
        db.commit()
        db.refresh(db_ability)
    except SQLAlchemyError as e:
        db.rollback()
        return 1
    return 0

def remove_all_abilities(db: Session):
    db.query(Ability).delete()
    db.commit()
