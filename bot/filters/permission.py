from aiogram.filters import Filter
from aiogram.types import TelegramObject
from sqlalchemy.orm import Session

from bot.decorators import create_session
from apps.general.choices import StaffType

from db import repository as repo
from db.schemas import StaffsTable


class Permission(Filter):
    roles = StaffType
    
    def __init__(self, permission_classes: list):
        self.permission_classes = [self.roles.ceo]
        self.permission_classes.extend(permission_classes)
        
    @create_session
    async def __call__(self, event: TelegramObject, session: Session, *args, **kwargs) -> bool:
        try:
            user_id = event.dict()['from_user']['id']
        except KeyError:
            return False

        user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)        
        if not user:
            return False

        staff: StaffsTable = await repo.StaffsTableRepository().get_staff(user_id=user.user_id, session=session)
        if staff:
            return staff.role in self.permission_classes

        return False
