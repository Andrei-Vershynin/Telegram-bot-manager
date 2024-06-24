import os
from aiogram.types.input_file import FSInputFile

def get_photo(file_name: str | None = None) -> FSInputFile:
    # path_to_loader = __file__ # /Users/nick/Desktop/Python/1730Online/final_bot/bot_modules/loader.py
    # path_to_bot_modules = os.path.abspath(path_to_loader + '/..') # /Users/nick/Desktop/Python/1730Online/final_bot/bot_modules
    # path_to_main_folder = os.path.abspath(path_to_bot_modules + '/..') # /Users/nick/Desktop/Python/1730Online/final_bot
    # path_to_image = os.path.abspath(path_to_main_folder + f'/static/images/{file_name}') #/Users/nick/Desktop/Python/1730Online/final_bot/static/images/orig.png
    # photo = FSInputFile(path= path_to_image)  
    # return photo
    return FSInputFile(os.path.abspath(__file__ + f"/../../static/images/{file_name}"))


