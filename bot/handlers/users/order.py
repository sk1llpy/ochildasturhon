import os

from aiogram import types, html, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext

from bot.routers import users as router
from bot.decorators import create_session
from bot.filters import Chat
from bot.keyboards.default import start
from bot.keyboards.inline import menu, quantity
from bot.states.buy import BuyFoodState

from db.config import Session
from db import repository as repo
from data.config import MEDIA_ROOT

from auth import UserHandling


_ = gettext

@router.callback_query(Chat().is_private(), StateFilter(BuyFoodState.food), lambda call: call.data.startswith("food_"))
@create_session
async def menu_handler(call: types.CallbackQuery, state: FSMContext, session: Session):
    data = {
        "user_id": call.from_user.id,
        "session": session
    }
    if await UserHandling(**data).user(False):
        food = await repo.FoodsTableRepository().get_food(call.data.split('food_')[-1], session)
        if food:
            await call.message.delete()
            await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
            await call.message.answer_photo(
                photo = types.FSInputFile(MEDIA_ROOT / food.image),
                caption = (f"""{html.bold(food.title + " — " + f"{food.price} {_('сум')}")}""" + "\n\n" +
                           html.italic(_("Miqdorni tanlang 👇"))
                ),
                reply_markup = await quantity.button()
            )

