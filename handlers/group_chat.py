from aiogram import Router, F, types

from helper import get_quote

router = Router()


@router.message(F.reply_to_message)
async def answer_to_reply(message: types.Message):
    print('@reply')
    return await message.reply(get_quote())


@router.message(F.text)
async def trigger_words(message: types.Message):
    print('@trigger')
    if 'сахар' in message.text.lower():
        return message.reply('Жри сахар')
    return message.answer('lol')
