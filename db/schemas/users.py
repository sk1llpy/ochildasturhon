from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.config import BaseModel
from apps.general.choices import LanguageType


# Create your tables here.
class UsersTable(BaseModel):
    __tablename__ = 'users_user'

    user_id: Mapped[int] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(nullable=True)
    banned: Mapped[bool] = mapped_column(default=False)

    admins: Mapped[list["StaffsTable"]] = relationship(back_populates="user")
    baskets: Mapped[list["BasketsTable"]] = relationship(back_populates="user")
    orders: Mapped[list["OrdersTable"]] = relationship(back_populates="user")


class StaffsTable(BaseModel):
    __tablename__ = 'users_staff'

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    dashboard_username: Mapped[str] = mapped_column()
    dashboard_password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["UsersTable"] = relationship(back_populates='admins')