from aiogram import types, html
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext
import logging

from bot.routers import users as router
from bot.decorators import create_session
from bot.filters import Chat
from bot.keyboards.default import start
from bot.keyboards.inline import language
from bot.states.register import RegisterState

from db.config import Session
from db import repository as repo

from apps.general.choices import StaffType
from auth import UserHandling

_ = gettext

@router.message(Chat().is_private(), CommandStart())
@create_session
async def start_handler(message: types.Message, state: FSMContext, session: Session):
    data = {
        "user_id": message.from_user.id,
        "session": session
    }

    if await UserHandling(**data).not_started_bot():
        await state.set_state(RegisterState.langauge)
        await message.answer(
            text=f"""{html.bold("Salom / Привет")} 👋

{html.italic("Tilni tanlang / Выберите язык 👇")}""",
            reply_markup=await language.button()
        )
    else:
        if await UserHandling(**data).user(True):
            await message.answer(
                text=f"""{html.bold(_("Привет") + " " + message.from_user.first_name)} 👋

{html.bold(_("Выберите нужный раздел 👇"))}""",
                reply_markup = await start.button()
            )
        elif await UserHandling(**data).manager():
            staff = await repo.StaffsTableRepository().get_staff(user_id=message.from_user.id,
                                                                 session=session)
            await message.answer(
                text=f"""{html.bold(_("Привет Админ -") + " " + message.from_user.first_name)} 👋

{html.bold(_("Выберите нужный раздел 👇"))}""",
                reply_markup = await start.button(True, staff.dashboard_username, staff.dashboard_password)
            )