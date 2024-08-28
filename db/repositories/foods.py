from sqlalchemy.orm import Session
from sqlalchemy import select

from db import repository as repo
from datetime import date as dt
from db.repository import BaseRepository
from db.schemas import FoodsTable


# create your repositories here.
class FoodsTableRepository(BaseRepository):
    table = FoodsTable

    async def today_foods(self, session: Session):
        with session:
            foods = (session.execute(
                select(FoodsTable).where(FoodsTable.date == dt.today())
            )).scalars().all()

            return foods
    
    async def get_food(self, food_id: int, session: Session):
        with session:
            food = (session.execute(
                select(FoodsTable).where(FoodsTable.id == food_id)
            )).scalar_one_or_none()

            return food
