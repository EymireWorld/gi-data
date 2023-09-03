from enum import StrEnum

from pydantic import BaseModel

from app.schemas import WeaponType


class WeaponSubstatType(StrEnum):
    attack = 'Attack %'
    critical_rate = 'Critical rate %'
    critical_damage = 'Critical damage %'
    defence = 'Defense %'
    health = 'Health %'
    elemental_mastery = 'Elemental mastery'
    energy_recharge = 'Energy recharge %'
    physical_damage = 'Physical damage %'


class Weapon(BaseModel):
    id: int
    name: str
    type: WeaponType
    rarity: int
    attack: int
    substat_name: WeaponSubstatType | None
    substat_value: float | None
    affix_name: str | None
    affix_description: list[str] | None
    description: str


class WeaponCreate(BaseModel):
    name: str
    type: WeaponType
    rarity: int
    attack: int
    substat_name: WeaponSubstatType | None
    substat_value: float | None
    affix_name: str | None
    affix_description: list[str] | None
    description: str


class WeaponUpdate(BaseModel):
    name: str = None
    type: WeaponType = None
    rarity: int = None
    attack: int = None
    substat_name: WeaponSubstatType | None = None
    substat_value: float | None = None
    affix_name: str | None = None
    affix_description: list[str] | None = None
    description: str = None
