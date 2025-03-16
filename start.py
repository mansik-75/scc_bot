import json
from aiogram.types import Update
from bot import init_bot
from handlers import group_chat, private_chat


bot, dp = init_bot()

dp.include_routers(private_chat.router, group_chat.router)


async def process_event(event, dispatcher):
    for message in event.get('messages', []):
        body = message.get('details', {}).get('message', {}).get('body')
        if body:
            update = Update(**json.loads(body))
            await dispatcher.feed_update(bot, update)


async def start(event, context):
    print(event)
    await process_event(event, dp)
    return {'statusCode': 200, 'body': 'ok'}
