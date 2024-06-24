from .dispatcher_bot import dispatcher
from .keyboards_bot import inline_main_keyboard
from aiogram.types import CallbackQuery
from .buttons_bot import list_inline_buttons, list_step
from .player import step_player
from .victory import victory_check
from .enemy_bot import step_bot

list_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

victory = ['']

@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery): 
    if callback.data in list_number:
        step = step_player(victory= victory, callback = callback)

        await victory_check(
            list_inline_buttons= list_inline_buttons,
            victory= victory,
            step= step,
            callback= callback,
            inline_main_keyboard= inline_main_keyboard,
            list_step= list_step,
        )
        # if callback.message.text != 'Переміг хрестик' or callback.message.text != 'Переміг нолик':
        if list_step != ' ':
            step = step_bot(victory= victory, callback = callback, inline_main_keyboard= inline_main_keyboard, list_step= list_step)

            await victory_check(
                list_inline_buttons= list_inline_buttons,
                victory= victory,
                step= step,
                callback= callback,
                inline_main_keyboard= inline_main_keyboard,
                list_step= list_step,
            )


    
