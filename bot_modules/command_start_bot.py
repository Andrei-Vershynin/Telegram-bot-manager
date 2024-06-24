from aiogram.filters import CommandStart
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .keyboards_bot import main_keyboard

@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text = "Hi, User!", reply_markup= main_keyboard)
    