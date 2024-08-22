from sqlalchemy.orm import Session

from db import repository as repo
from db.repository import BaseRepository
from db.schemas import UsersTable, StaffsTable


# create your repositories here.
class UsersTableRepository(BaseRepository):
    table = UsersTable

    async def get_user(self, user_id: int, session: Session) -> table:
        return self.get("user_id", user_id, session=session)
    
    async def create_user(self, session: Session, **user_data):
        user = await self.get_user(user_id=user_data['user_id'], session=session)

        if not user:
            return self.create(user_data, session)
    
    async def update_user(self, session: Session, **user_data):
        user = await self.get_user(user_id=user_data['user_id'], session=session)

        if user:
            return self.edit(conditions={"user_id": user.user_id}, edits=user_data, session=session)


class StaffsTableRepository(BaseRepository):
    table = StaffsTable

    async def get_staff(self, user_id: int, session: Session) -> table:
        user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)

        return self.get("user_id", user.id, session=session)