from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from . import services
from .schemas import Weapon, WeaponCreate, WeaponUpdate

router = APIRouter()


@router.get('', response_model = list[Weapon])
async def get_weapons(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await services.get_weapons(offset, limit, db)


@router.post('', response_model = Weapon)
async def create_weapon(data: WeaponCreate, db: AsyncSession = Depends(get_db)):
    return await services.create_weapon(data, db)


@router.get('/{weapon_id}', response_model = Weapon)
async def get_weapon(weapon_id: int, db: AsyncSession = Depends(get_db)):
    return await services.get_weapon(weapon_id, db)


@router.put('/{weapon_id}', response_model = Weapon)
async def update_weapon(weapon_id: int, data: WeaponUpdate, db: AsyncSession = Depends(get_db)):
    return await services.update_weapon(weapon_id, data, db)


@router.delete('/{weapon_id}', response_model = Weapon)
async def delete_weapon(weapon_id: int, db: AsyncSession = Depends(get_db)):
    return await services.delete_weapon(weapon_id, db)
