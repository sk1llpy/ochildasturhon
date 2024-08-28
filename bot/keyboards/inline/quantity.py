from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext
from . import back

_ = gettext

async def button(num: int = 0) -> InlineKeyboardMarkup:
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"➖", callback_data='decrease'),
                InlineKeyboardButton(text=f"{num}", callback_data='num'),
                InlineKeyboardButton(text=f"➕", callback_data='increase')
            ]
        ]
    )
    button.inline_keyboard.extend((await back.button()).inline_keyboard)
    return button