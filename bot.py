import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


def init_bot():
    bot = Bot(token=os.environ.get('API_TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())

    return bot, dp
