from db import repository as repo
from sqlalchemy.orm import Session
from apps.general.choices import StaffType


roles_rating = {
    "courier": 1,
    "cook": 1,
    "call_center": 1,
    "manager": 2,
    "admin": 3,
    "ceo": 4
}

class UserHandling:
    def __init__(self, user_id: int, session: Session) -> None:
        self.user_id = user_id
        self.session = session
        self.user_data = None
        self.staff_data = None
        self.result = False
    
    async def init_data(self):
        self.user_data = await repo.UsersTableRepository().get_user(user_id=self.user_id, session=self.session)
        self.result = True if self.user_data else False
        if self.result:
            self.staff_data = await repo.StaffsTableRepository().get_staff(user_id=self.user_data.user_id, session=self.session)

    async def user(self, only: bool = False):
        await self.init_data()
        if self.result:
            if only:
                return True if not self.staff_data else False
            else:
                return True
        else:
            return False

    async def courier(self, only: bool = False):
        return await self._check_role(StaffType.courier, only)

    async def cook(self, only: bool = False):
        return await self._check_role(StaffType.cook, only)

    async def call_center(self, only: bool = False):
        return await self._check_role(StaffType.call_center, only)

    async def manager(self, only: bool = False):
        return await self._check_role(StaffType.manager, only)

    async def admin(self, only: bool = False):
        return await self._check_role(StaffType.admin, only)

    async def ceo(self, only: bool = False):
        return await self._check_role(StaffType.ceo, only)

    async def _check_role(self, role: StaffType, only: bool = False):
        await self.init_data()
        if self.result and self.staff_data:
            if only:
                return self.staff_data.role == role
            else:
                return roles_rating[self.staff_data.role] <= roles_rating[role]
        else:
            return False

    async def not_started_bot(self):
        await self.init_data()
        return self.user_data == None