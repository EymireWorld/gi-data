from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Weapon as WeaponModel
from .schemas import WeaponCreate as WeaponCreateSchema, WeaponUpdate as WeaponUpdateSchema


async def create_weapon(data: WeaponCreateSchema, db: AsyncSession):
    result = await db.execute(
        insert(WeaponModel).values(data.model_dump(exclude_unset = True)).returning(WeaponModel)
    )
    await db.commit()

    return result.scalar()


async def get_weapons(offset: int, limit: int, db: AsyncSession):
    result = await db.execute(
        select(WeaponModel)
    )

    return result.scalars().all()[offset:][:limit]


async def get_weapon(weapon_id: int, db: AsyncSession):
    result = await db.execute(
        select(WeaponModel).where(WeaponModel.id == weapon_id)
    )

    return result.scalar()


async def update_weapon(weapon_id: int, data: WeaponUpdateSchema, db: AsyncSession):
    result = await db.execute(
        update(WeaponModel).where(WeaponModel.id == weapon_id).values(data.model_dump(exclude_unset = True)).returning(
            WeaponModel)
    )
    await db.commit()

    return result.scalar()


async def delete_weapon(weapon_id: int, db: AsyncSession):
    result = await db.execute(
        delete(WeaponModel).where(WeaponModel.id == weapon_id).returning(WeaponModel)
    )
    await db.commit()

    return result.scalar()
