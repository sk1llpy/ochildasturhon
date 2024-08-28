from sqlalchemy.orm import Session

from db import repository as repo
from db.repository import BaseRepository
from db.schemas import OrdersTable, OrderFoodTable


# create your repositories here.
class OrdersTableRepository(BaseRepository):
    table = OrdersTable


class OrderFoodTableRepository(BaseRepository):
    table = OrderFoodTable
