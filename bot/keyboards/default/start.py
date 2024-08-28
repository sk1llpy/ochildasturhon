from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.i18n import gettext
from sqlalchemy.orm import Session

from bot.misc import bot_settings
from auth import UserHandling

_ = gettext

async def button(user_id: int, session: Session, username: str = None, password: str = None):
    if await UserHandling(user_id, session).manager():
        keyboard = [
            [
                KeyboardButton(
                    text = _("📲 Админ-панель"), 
                    web_app = WebAppInfo(
                        url = f"{bot_settings.web_app_url}/admin/login/{username}/{password}"
                    )
                )
            ],
            [
                KeyboardButton(text=_("🍽 Меню")),
                KeyboardButton(text=_("➕ Добавить еду"))
            ],
            [
                KeyboardButton(text=_("💸 Ежемесячный отчет"))
            ],
            [
                KeyboardButton(text=_("✍️ Изменить еду")),
                KeyboardButton(text=_("❌ Удалит еду"))
            ],
            [
                KeyboardButton(text=_("📨 Отправьте пользователей к сегодняшнему меню")),
                KeyboardButton(text=_("📥 Отправить сообщение"))
            ],
            [
                KeyboardButton(text=_("⚙️ Настройки"))
            ]
        ]
        
    elif await UserHandling(user_id, session).cook(True):
        keyboard = [
            [
                KeyboardButton(text=_("🍽 Меню")),
                KeyboardButton(text=_("➕ Добавить еду"))
            ],
            [
                KeyboardButton(text=_("📨 Отправьте пользователей к сегодняшнему меню"))
            ],
            [
                KeyboardButton(text=_("✍️ Изменить еду")),
                KeyboardButton(text=_("❌ Удалит еду"))
            ],
            [
                KeyboardButton(text=_("⚙️ Настройки"))
            ]
        ]

    elif await UserHandling(user_id, session).user(True):
        keyboard = [
            [
                KeyboardButton(text = _("🍽 Меню"))
            ],
            [
                KeyboardButton(text = _("🔄 История заказов")),
                KeyboardButton(text = _("📍 Локации"))
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