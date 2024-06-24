from aiogram.filters import CommandStart
from .dispatcher_bot import dispatcher
from aiogram.types import Message 
from .keyboards_bot import inline_keyboard

@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text= "Привіт, користувач", reply_markup= inline_keyboard)
    for el in message:
        print(el)