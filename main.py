import asyncio
import logging

from dotenv import load_dotenv

from bot import init_bot
from handlers import group_chat, private_chat


async def main():
    load_dotenv()
    logging.basicConfig(level=logging.DEBUG)

    bot, dp = init_bot()

    dp.include_routers(private_chat.router, group_chat.router)

    print('SCC bot started')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
