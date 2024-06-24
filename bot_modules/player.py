from .buttons_bot import list_inline_buttons, list_step
from .keyboards_bot import inline_main_keyboard
from aiogram.types import CallbackQuery

def step_player(victory: list, callback: CallbackQuery ):
    if list_step[0] == "хрестик":
        step = 'X'
        list_step[0] = 'нолик'
        victory[0] = 'хрестик'
    elif list_step[0] == "нолик":
        step = 'O'
        list_step[0] = 'хрестик'
        victory[0] = 'нолик'
        #
    button = list_inline_buttons[int(callback.data)]
    #
    inline_main_keyboard.inline_keyboard[button.row_button][button.number_button].text = step
    inline_main_keyboard.inline_keyboard[button.row_button][button.number_button].callback_data = step

    return step