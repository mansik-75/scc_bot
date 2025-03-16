import os
import random

from aiogram import Router, F, types
from dotenv import load_dotenv

from helper import get_quote

router = Router()
load_dotenv()


@router.message(F.reply_to_message)
async def answer_to_reply(message: types.Message):
    print('@reply')
    return await message.reply(get_quote())


@router.message(F.text)
async def trigger_words(message: types.Message):
    print('@trigger')
    if 'сахар' in message.text.lower():
        return message.reply('Жри сахар')
    n = random.randint(0, 100)
    if n > int(os.environ.get('ANSWER_PROB') or 0):
        return message.answer(get_quote())
