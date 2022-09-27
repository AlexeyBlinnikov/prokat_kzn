from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('/Загрузить')
button_load1 = KeyboardButton('/Загрузить_онлайн')
button_delete = KeyboardButton('/Удалить')
button_delete1 = KeyboardButton('/Удалить_онлайн')

kb_admin = ReplyKeyboardMarkup(resize_keyboard = True).add(button_load).add(button_delete).add(button_load1).add(button_delete1)