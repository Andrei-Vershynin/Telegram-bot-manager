import aiogram

start_game = aiogram.types.KeyboardButton(text = "Почати гру")
cross_button = aiogram.types.KeyboardButton(text = "Хрестик")
zero_button = aiogram.types.KeyboardButton(text = "Нолик")

list_inline_buttons = []
list_step = []
# inline_information_button = aiogram.types.InlineKeyboardButton(text = "ходить", callback_data = "0")

number = 0
row = 0
for count in range(0, 9):
    
    inline_button = aiogram.types.InlineKeyboardButton(text = " ", callback_data = f"{count}", number_button = number, row_button = row)
    number += 1
    if number > 2:
        number = 0
        row += 1
    list_inline_buttons.append(inline_button)
    