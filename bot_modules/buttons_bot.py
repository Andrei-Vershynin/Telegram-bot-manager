import aiogram 

button_start = aiogram.types.KeyboardButton(text = "START")

button_users = aiogram.types.InlineKeyboardButton(text="GET USERS", callback_data= "user")
button_products = aiogram.types.InlineKeyboardButton(text="GET PRODUCTS", callback_data="products")
button_cart = aiogram.types.InlineKeyboardButton(text="GET CART", callback_data="cart")
button_add_product = aiogram.types.InlineKeyboardButton(text="ADD PRODUCT", callback_data="add_product")

button_delete_user = aiogram.types.InlineKeyboardButton(text = "DELETE USER", callback_data = "delete_user" )
button_set_admin = aiogram.types.InlineKeyboardButton(text = "SET ADMIN", callback_data= "admin_user")