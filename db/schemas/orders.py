from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date as dt

from db.config import BaseModel


# Create your tables here.
class BasketsTable(BaseModel):
    __tablename__ = 'orders_basket'

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    food_id: Mapped[int] = mapped_column(ForeignKey('foods_food.id'))

    user: Mapped["UsersTable"] = relationship(back_populates="baskets")
    food: Mapped["FoodsTable"] = relationship(back_populates="baskets")


class OrderFoodTable(BaseModel):
    __tablename__ = 'orders_orderfood'

    order_id: Mapped[int] = mapped_column(ForeignKey('orders_order.id'))
    food_id: Mapped[int] = mapped_column(ForeignKey('foods_food.id'))

    order: Mapped["OrdersTable"] = relationship(back_populates="order_foods")
    food: Mapped["FoodsTable"] = relationship(back_populates="order_foods")


class OrdersTable(BaseModel):
    __tablename__ = 'orders_order'

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    status: Mapped[str] = mapped_column()
    location: Mapped[str] = mapped_column()

    user: Mapped["UsersTable"] = relationship(back_populates="orders")
    order_foods: Mapped[list["OrderFoodTable"]] = relationship(back_populates="order")