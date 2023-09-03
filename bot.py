import asyncio
from aiogram import Bot, Dispatcher, F
from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers


async def main():

    config: Config = load_config()

    bot: Bot = Bot(config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_routers(user_handlers.router, other_handlers.router)
     
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('все подключается!')
    asyncio.run(main())
    

