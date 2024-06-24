import aiogram
from .buttons_bot import start_game, list_inline_buttons

main_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard= [[start_game]],
    one_time_keyboard= True
)

inline_main_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard = [
        [list_inline_buttons[0], list_inline_buttons[1], list_inline_buttons[2]],
        [list_inline_buttons[3], list_inline_buttons[4], list_inline_buttons[5]],
        [list_inline_buttons[6], list_inline_buttons[7], list_inline_buttons[8]]
    ]
)