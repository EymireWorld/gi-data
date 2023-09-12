from sqlalchemy import Column, Enum, Float, Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY as Array

from app.database import Base
from app.schemas import WeaponType
from .schemas import WeaponSubstatType


class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String, nullable = False)
    image_url = Column(String, nullable = False)
    type = Column(Enum(WeaponType), nullable = False)
    rarity = Column(SmallInteger, nullable = False)
    attack = Column(SmallInteger, nullable = False)
    substat_name = Column(Enum(WeaponSubstatType), nullable = True)
    substat_value = Column(Float, nullable = True)
    affix_name = Column(String, nullable = True)
    affix_description = Column(Array(String), nullable = True)
