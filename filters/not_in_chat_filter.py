from aiogram.types import Message
from aiogram.filters import Filter


class NotInChatFilter(Filter):
    def __init__(self, forbidden_chat_id: int | list[int]):
        self.forbidden_chat_ids = [forbidden_chat_id] if isinstance(forbidden_chat_id, int) else forbidden_chat_id

    async def __call__(self, message: Message) -> bool:
        return message.chat.id not in self.forbidden_chat_ids
