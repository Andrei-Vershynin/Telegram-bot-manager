from aiogram.types import CallbackQuery, InlineKeyboardMarkup

async def victory_check(list_inline_buttons: list, victory: list, step: str, callback: CallbackQuery, inline_main_keyboard: InlineKeyboardMarkup, list_step: list):
    #
    if list_inline_buttons[0].callback_data == step and list_inline_buttons[3].callback_data == step and list_inline_buttons[6].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    elif list_inline_buttons[1].callback_data == step and list_inline_buttons[4].callback_data == step and list_inline_buttons[7].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    elif list_inline_buttons[2].callback_data == step and list_inline_buttons[5].callback_data == step and list_inline_buttons[8].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    # додати три переможні варіанти для горизонтальної перемоги
    elif list_inline_buttons[0].callback_data == step and list_inline_buttons[1].callback_data == step and list_inline_buttons[2].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    elif list_inline_buttons[3].callback_data == step and list_inline_buttons[4].callback_data == step and list_inline_buttons[5].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    elif list_inline_buttons[6].callback_data == step and list_inline_buttons[7].callback_data == step and list_inline_buttons[8].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    # додати два переможні варіанти для діагональної перемоги 
    elif list_inline_buttons[0].callback_data == step and list_inline_buttons[4].callback_data == step and list_inline_buttons[8].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    elif list_inline_buttons[2].callback_data == step and list_inline_buttons[4].callback_data == step and list_inline_buttons[6].callback_data == step:
        await callback.message.edit_text(text= f"Переміг {victory[0]}")
        list_step[0] = ' '
    #
    else:
        await callback.message.edit_text(text= f"Ходить {list_step[0]}", reply_markup= inline_main_keyboard)