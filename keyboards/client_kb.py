from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Сапы')
b2 = KeyboardButton('/Туристическое_оборудование')
b3 = KeyboardButton('/Расположение')
b4 = KeyboardButton('/Режим_работы')
# b4 = KeyboardButton('/Показать где я', request_location = True)
# b5 = KeyboardButton('/ПОделиться номером', request_contact = True)

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.add(b1).add(b2).add(b3).add(b4)#.add(b5)