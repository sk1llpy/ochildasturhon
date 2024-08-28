from aiogram import types, html, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext

from bot.routers import users as router
from bot.decorators import create_session
from bot.filters import Chat
from bot.keyboards.default import start
from bot.keyboards.inline import menu
from bot.states.buy import BuyFoodState

from db.config import Session
from db import repository as repo
from data.config import MEDIA_ROOT

from apps.general.choices import StaffType
from auth import UserHandling

_ = gettext

@router.message(Chat().is_private(), F.text.in_(["🍽 Меню"]))
@create_session
async def menu_handler(message: types.Message, state: FSMContext, session: Session):
    data = {
        "user_id": message.from_user.id,
        "session": session
    }
    if await UserHandling(**data).user(False):
        foods = await repo.FoodsTableRepository().today_foods(session=session)

        if foods:
            await state.set_state(BuyFoodState.food)
            await (await message.answer(".", reply_markup=types.ReplyKeyboardRemove())).delete()

            text = html.bold(_("Assalomu alaykum! Bugungi menyu 👇")) + "\n\n"
            media: list[types.InputMediaPhoto] = []
            for food in foods:
                text += f"🫕 {food.title} — {food.price} so'm\n"
                media.append(
                    types.InputMediaPhoto(
                        media = types.FSInputFile(MEDIA_ROOT / food.image)
                    )
                )
            text += "\n\n" + html.italic("\n🚗 Yetkazib berish Yandex Go yordamida amalga oshiriladi.")

            await message.answer_media_group(
                media=media,
            )
            await message.answer(
                text = text, 
                reply_markup = await menu.button([(food.id, food.title, food.price) for food in foods])
            )
        else:
            await message.answer(
                html.bold(_("Ovqatlar mavjud emas ❌"))
            )
        
