import io

from aiogram import types, F, Router, Bot
from aiogram.filters import Command
from aiogram.types import BufferedInputFile
from dotenv import load_dotenv

from filters.chat_type_filter import ChatTypeFilter
from helper import save_file
from readers import read_gpx

load_dotenv()

router = Router()
router.message.filter(ChatTypeFilter(chat_type=['private']))
# router.message.filter(lambda x: False)


@router.message(Command('start'))
@router.message(F.text)
async def cmd_start(message: types.Message):
    return await message.answer('Привет, пока я могу немного: скинь мне маршрут в формате .gpx')


@router.message(F.document)
async def process_document(message: types.Message, bot: Bot):
    format_processors = {
        'gpx': read_gpx
    }
    filename = message.document.file_name
    file_format = filename.split('.')[-1]
    if file_format not in format_processors:
        return await message.answer(f"Пока я не умею читать данный формат, пришли что-то из этого: {', '.join(format_processors.keys())}")

    file_in_io = io.BytesIO()
    await bot.download(message.document, file_in_io)
    file_in_io.name = filename
    file_in_io.seek(0)

    latitude, longitude = format_processors[file_format](file_in_io.read().decode('utf8'))

    image = save_file(latitude, longitude)


    await message.answer_document(
        BufferedInputFile(
            image.read(),
            filename= '.'.join(filename.split('.')[:-1]) + '.png',
        ),
        caption="Картинка по полученному маршруту"
    )
