from enum import StrEnum

from pydantic import BaseModel, HttpUrl, field_serializer
from pydantic_core import Url

from app.schemas import WeaponType


class WeaponSubstatType(StrEnum):
    attack = 'Attack %'
    critical_rate = 'Critical Rate %'
    critical_damage = 'Critical Damage %'
    defence = 'Defense %'
    health = 'Health %'
    elemental_mastery = 'Elemental Mastery'
    energy_recharge = 'Energy Recharge %'
    physical_damage = 'Physical Damage %'


class Weapon(BaseModel):
    id: int
    name: str
    image_url: HttpUrl
    type: WeaponType
    rarity: int
    attack: int
    substat_name: WeaponSubstatType | None
    substat_value: float | None
    affix_name: str | None
    affix_description: list[str] | None

    @field_serializer('image_url')
    def url_to_str(self, val) -> str:
        if isinstance(val, Url):
            return str(val)
        return val


class WeaponCreate(BaseModel):
    name: str
    image_url: HttpUrl
    type: WeaponType
    rarity: int
    attack: int
    substat_name: WeaponSubstatType | None = None
    substat_value: float | None = None
    affix_name: str | None = None
    affix_description: list[str] | None = None

    @field_serializer('image_url')
    def url_to_str(self, val) -> str:
        if isinstance(val, Url):
            return str(val)
        return val


class WeaponUpdate(BaseModel):
    name: str = None
    image_url: HttpUrl = None
    type: WeaponType = None
    rarity: int = None
    attack: int = None
    substat_name: WeaponSubstatType | None = None
    substat_value: float | None = None
    affix_name: str | None = None
    affix_description: list[str] | None = None

    @field_serializer('image_url')
    def url_to_str(self, val) -> str:
        if isinstance(val, Url):
            return str(val)
        return val
