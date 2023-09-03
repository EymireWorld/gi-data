from fastapi import FastAPI

from .weapon.router import router as weapon_router

app = FastAPI()
app.include_router(
    weapon_router,
    prefix = '/weapon',
    tags = ['weapon']
)
