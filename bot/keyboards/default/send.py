from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext

_ = gettext

async def button(type: bool = True):
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=_("📞 Отправить номер телефона"), request_contact=True)
            ]
        ]
    ) if type else ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=_("📍 Отправить местоположение"), request_location=True)
            ]
        ]
    )