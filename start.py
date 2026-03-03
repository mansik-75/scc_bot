import json
from aiogram.types import Update
from bot import init_bot
from handlers import group_chat

bot, dp = init_bot()

dp.include_routers(group_chat.router)


async def process_event(body, dispatcher):
    if body:
        update = Update(**json.loads(body))
        await dispatcher.feed_update(bot, update)


async def start(event, _):
    print(event)
    await process_event(event['body'], dp)
    return {'statusCode': 200, 'body': 'ok'}
