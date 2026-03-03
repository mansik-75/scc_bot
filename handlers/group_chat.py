import os
import random

from aiogram import Router, F, types
from dotenv import load_dotenv

from filters.chat_type_filter import ChatTypeFilter
from filters.not_in_chat_filter import NotInChatFilter
from helper import get_quote

router = Router()
router.message.filter(NotInChatFilter(forbidden_chat_id=-1001788767428))
router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]),)

load_dotenv()


@router.message(F.text.lower().contains('шамс'))
@router.message(F.text.lower().contains('щамс'))
@router.message(F.text.lower().contains('шəмс'))
@router.message(F.text.lower().contains('щəмс'))
async def fine_trigger(message: types.Message):
    if 'шамсат' in message.text.lower():
        return
    return await message.reply_sticker(os.environ.get('FINE_FILE_ID'))


@router.message(F.text.lower().contains('сахар'))
async def trigger_sugar(message: types.Message):
    n = random.randint(0, 100)
    if n < 20:
        return await message.reply('Жри сахар')


@router.message(F.text.contains('ФОРМАТ КРУТО'))
async def trigger_format_correct(message: types.Message):
    return await message.reply('этот шарит')


@router.message(F.text.lower().contains('формат'))
async def trigger_format_incorrect(message: types.Message):
    n = random.randint(0, 100)
    if n < 50:
        return await message.reply('ФОРМАТ КРУТО')


@router.message(F.text.lower().contains('ftp'))
@router.message(F.text.lower().contains('фтп'))
async def trigger_ftp(message: types.Message):
    return await message.reply('мнение людей с фтп меньше 4 не учитывается')


@router.message(F.text.lower().contains('потемнело'))
@router.message(F.text.lower().contains('обморок'))
async def trigger_base(message: types.Message):
    return await message.reply('вот что БАЗА животворящая делает')


@router.message(F.reply_to_message.is_topic_message)
@router.message(F.reply_to_message)
async def answer_to_reply(message: types.Message):
    if message.reply_to_message.from_user.username != 'snailcc_bot':
        return
    print('@reply')
    return await message.reply(get_quote())


@router.message(F.text)
async def trigger_straight(message: types.Message):
    print('@trigger')
    n = random.randint(0, 100)
    if n < int(os.environ.get('ANSWER_PROB') or 0):
        return await message.answer(get_quote())
