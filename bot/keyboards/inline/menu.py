from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext
from . import back

_ = gettext

async def button(foods: list = []):
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{food[1]} — {food[2]} {_('сум')}", callback_data=f'food_{food[0]}')
            ] for food in foods
        ]
    )
    button.inline_keyboard.extend((await back.button()).inline_keyboard)
    
    return button