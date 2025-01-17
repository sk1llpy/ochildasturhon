from bot.misc import dp, bot
from bot.utils import logging, include_routers, setup
from bot import handlers


async def polling():
    await setup.setup_middlewares(dispatcher=dp)
    await setup.setup_filters(dispatcher=dp)

    await include_routers.include_routers()
    
    await dp.start_polling(bot)