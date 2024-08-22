from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.i18n import gettext

from bot.misc import bot_settings

_ = gettext

async def button(admin: bool = False, username: str = None, password: str = None):
    if admin:
        keyboard = [
            [
                KeyboardButton(
                    text = _("📲 Админ-панель"), 
                    web_app = WebAppInfo(
                        url = f"{bot_settings.web_app_url}/admin/login/{username}/{password}"
                    )
                )
            ]
        ]
    else:
        keyboard = [
            [
                KeyboardButton(text = _("🍽 Меню"))
            ],
            [
                KeyboardButton(text = _("🔄 История заказов")),
                KeyboardButton(text = _("Филиалы"))
            ],
            [
                KeyboardButton(text = _("📍 Мои местоположения"))
            ],
            [
                KeyboardButton(text = _("✍️ Оставить отзыв")),
                KeyboardButton(text = _("☎️ Связаться с нами"))
            ],
            [
                KeyboardButton(text = _("⚙️ Настройки"))
            ]
        ]

    return ReplyKeyboardMarkup(
        resize_keyboard = True,
        one_time_keyboard = True,
        keyboard = keyboard
    )