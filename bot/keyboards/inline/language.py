from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def button() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
            ]
        ]
    )