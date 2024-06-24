import aiogram 
from .buttons_bot import button_users, button_delete_user, button_set_admin, button_cart, button_products, button_add_product


inline_keyboard= aiogram.types.InlineKeyboardMarkup(
    inline_keyboard=[
        [button_users, button_products],
        [button_cart, button_add_product]
    ]
)
user_inline_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard= [
        [button_delete_user, button_set_admin]
    ]
)
# product_inline_keyboard = aiogram.types.InlineKeyboardButton(
    # inline_keyboard=[
        # []
    # ]
# )