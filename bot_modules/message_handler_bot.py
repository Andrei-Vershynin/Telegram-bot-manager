from .dispatcher_bot import dispatcher
from aiogram.types import Message
from .keyboards_bot import main_keyboard, inline_main_keyboard
from .buttons_bot import cross_button, zero_button, list_step, list_inline_buttons

@dispatcher.message()
async def message_handler(message: Message):
    if message.text == "Почати гру":
        main_keyboard.keyboard[0] = [cross_button, zero_button]
        await message.answer(text = "Гру розпочато  Николай жучара", reply_markup= main_keyboard)
    elif message.text.lower() == "хрестик" or message.text.lower() == "нолик":
        list_step.append(message.text.lower())
        count = 0
        for inline_button in list_inline_buttons:
            inline_button.text = ' '
            inline_button.callback_data = f'{count}'
            count += 1
        await message.answer(text = f"Гравець грає за {message.text}", reply_markup= inline_main_keyboard)