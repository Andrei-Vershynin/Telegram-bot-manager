from .dispatcher_bot import dispatcher
from aiogram.types import Message
from .create_bot import bot
import os

path_folder_images = os.path.abspath(__file__ + '/../../images')\

@dispatcher.message()
async def message_handler(message: Message):
    if message.photo:
        print(f'photo = {message.photo[-1]}')
        file_id = message.photo[-1].file_id
        print(f"file_id = {file_id}")
        photo = await bot.get_file(file_id = file_id)
        photo_path = photo.file_path
        await bot.download_file(file_path = photo_path, destination = f'{path_folder_images}/1.png')
        