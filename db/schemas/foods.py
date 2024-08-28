from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date as dt

from db.config import BaseModel


# Create your tables here.
class FoodsTable(BaseModel):
    __tablename__ = 'foods_food'

    title: Mapped[str] = mapped_column()
    image: Mapped[str]
    date: Mapped[dt] = mapped_column()
    price: Mapped[int] = mapped_column()

    baskets: Mapped[list["BasketsTable"]] = relationship(back_populates="food")
    order_foods: Mapped[list["OrderFoodTable"]] = relationship(back_populates="food")
