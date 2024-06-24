from .buttons_bot import list_inline_buttons, list_step
import random
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from .keyboards_bot import inline_main_keyboard

def step_bot(victory: list, callback: CallbackQuery, inline_main_keyboard: InlineKeyboardMarkup, list_step: list):
    if list_step[0] == "хрестик":
        step = 'X'
        list_step[0] = 'нолик'
        victory[0] = 'хрестик'
    elif list_step[0] == "нолик":
        step = 'O'
        list_step[0] = 'хрестик'
        victory[0] = 'нолик'

    while True:   
        row = random.randint(0, 2)
        index_button = random.randint(0, 2)
        if inline_main_keyboard.inline_keyboard[row][index_button].callback_data != 'X' and inline_main_keyboard.inline_keyboard[row][index_button].callback_data != 'O':
            inline_main_keyboard.inline_keyboard[row][index_button].text = step
            inline_main_keyboard.inline_keyboard[row][index_button].callback_data = step
            break
        
    return step
