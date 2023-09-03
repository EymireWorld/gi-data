from sqlalchemy import Column, Enum, Float, Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY

from app.database import Base
from app.schemas import WeaponType
from .schemas import WeaponSubstatType


class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    type = Column(Enum(WeaponType))
    rarity = Column(SmallInteger)
    attack = Column(SmallInteger)
    substat_name = Column(Enum(WeaponSubstatType))
    substat_value = Column(Float)
    affix_name = Column(String)
    affix_description = Column(ARRAY(String))
    description = Column(String)
