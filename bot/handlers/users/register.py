from aiogram import types, html, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext

from bot.routers import users as router
from bot.decorators import create_session
from bot.filters import Chat, ContentType
from bot.keyboards.default import start, send
from bot.states.register import RegisterState

from db.config import Session
from db import repository as repo

from apps.general.choices import StaffType
from auth import UserHandling

_ = gettext


@router.callback_query(Chat().is_private(), F.data.in_(["uz", "ru"]), StateFilter(RegisterState.langauge))
async def register_language_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    await state.set_state(RegisterState.phone_number)

    await call.message.edit_text(
        text=f"""{html.bold(_("Русский язык выбран."))} """)
    await call.message.answer(
        text=html.bold(_("Отправьте свой номер телефона 👇")),
        reply_markup=await send.button(True))


@router.message(Chat().is_private(), ContentType(ContentType.CONTACT), StateFilter(RegisterState.phone_number))
@create_session
async def register_phone_number_handler(message: types.Message, state: FSMContext, session: Session):
    state_data = await state.get_data()

    user = message.from_user
    user_data = {
        "user_id": user.id,
        "username": user.username,
        "full_name": user.full_name,
        "phone_number": message.contact.phone_number,
        "language": state_data['language']
    }
    await repo.UsersTableRepository().create_user(
        session=session,
        **user_data
    )

    await state.clear()
    await message.answer(
        text=f"""{html.bold(_("Привет") + " " + message.from_user.first_name)} 👋

{html.bold(_("Выберите нужный раздел 👇"))}""",
        reply_markup = await start.button()
    )