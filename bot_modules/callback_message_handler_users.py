from .dispatcher_bot import dispatcher
from .create_bot import bot
from aiogram.types import CallbackQuery
from .keyboards_bot import user_inline_keyboard
import sqlite3 
from .buttons_bot import button_delete_user, button_set_admin

# chat_id_ = "-1002230106379"

@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):
    # 
    data_base = sqlite3.connect(database= 'instance/data.db')
    cursor = data_base.cursor()
    # 
    if callback.data == "user":
        cursor.execute("SELECT * FROM user")
        list_users = cursor.fetchall() 
        # list_users = [
        #   (1, 'Nick', '123', 0),
        #   (2, 'Nick', '123', 1),
        #   
        #   (4, 'Nick', '123', 0),
        #   (5, 'Nick', '123', 1),
        #  ]
        for user in list_users: # user = [1, 'Nick', '123', 0]
            button_delete_user.callback_data= f"delete_user_{user[0]}"
            #
            if int(user[3]) == 0:
                button_set_admin.callback_data= f"make_admin_{user[0]}"
                button_set_admin.text = "MAKE ADMIN"
            else:
                button_set_admin.callback_data= f"remove_admin_{user[0]}"
                button_set_admin.text = "REMOVE ADMIN"
            #
            # await callback.message.answer(
                # text= f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[2]} \nIs_admin: {user[3]}",
                # reply_markup= user_inline_keyboard
            # )
            await bot.send_message(
                chat_id= callback.message.chat.id, 
                message_thread_id= 2,
                text= f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[2]} \nIs_admin: {user[3]}",
                reply_markup= user_inline_keyboard
            )
    #
    elif "add_product" == callback.data:
        await bot.send_message(chat_id= callback.message.chat.id, text= "ADD PRODUCT", message_thread_id= 25)

    #
    elif "delete_user" in callback.data:
        id_user = int(callback.data.split("_")[-1]) # callback.data =  'delete_user_1' =>  id_user = ['delete', 'user', '1'] => id_user = 1
        #
        button_delete_user.callback_data = f'yes_{id_user}'
        button_delete_user.text = 'YES'
        
        button_set_admin.callback_data = f'no_{id_user}'
        button_set_admin.text = 'NO'
        user_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_set_admin]
        await callback.message.edit_reply_markup(inline_message_id= callback.inline_message_id, reply_markup= user_inline_keyboard)
    #
    elif 'yes' in callback.data:
        id_user = int(callback.data.split("_")[-1])
        cursor.execute("DELETE FROM user WHERE id = ?", [id_user]) 
        await callback.message.delete()
        button_delete_user.callback_data = f"delete_user_{id_user}"
        button_delete_user.text = "DELETE USER"
    #
    elif "no" in callback.data:
        id_user = int(callback.data.split("_")[-1])
        button_delete_user.callback_data = f"delete_user_{id_user}"
        button_delete_user.text = "DELETE USER"
        cursor.execute("SELECT * FROM user WHERE id = ?", [id_user])
        user = cursor.fetchall()[-1]
        if user == 0:
            button_set_admin.text = "MAKE ADMIN"
            button_set_admin.callback_data = f"make_admin_{id_user}"
        else:
            button_set_admin.text = "REMOVE ADMIN"
            button_set_admin.callback_data = f"remove_admin_{id_user}"

        user_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_set_admin]
        await callback.message.edit_reply_markup(inline_message_id = callback.inline_message_id, reply_markup = user_inline_keyboard)
    #
    elif "make_admin" in callback.data:
        id_user = int(callback.data.split("_")[-1])
        #
        cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", [1, id_user])
        #
        button_set_admin.callback_data= f"remove_admin_{id_user}"
        button_set_admin.text = "REMOVE ADMIN"
        #
        cursor.execute("SELECT * FROM user WHERE id = ?", [id_user])
        user = cursor.fetchall()[0]
        await callback.message.edit_text(
            text = f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[2]} \n➡️Is_admin: {user[3]}⚠️", 
            reply_markup= user_inline_keyboard
        )
    #
    elif "remove_admin" in callback.data:
        id_user = int(callback.data.split("_")[-1])
        #
        cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", [0, id_user])
        #
        button_set_admin.callback_data= f"make_admin_{id_user}"
        button_set_admin.text = "MAKE ADMIN"
        #
        cursor.execute("SELECT * FROM user WHERE id = ?", [id_user])
        user = cursor.fetchall()[0]
        await callback.message.edit_text(
            text = f"ID: {user[0]} \nName: {user[1]} \nPassword: {user[2]} \n➡️Is_admin: {user[3]}", 
            reply_markup= user_inline_keyboard
        )
    # 
    data_base.commit()
    data_base.close()
