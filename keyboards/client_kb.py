from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('🏕️ Оборудование 🏄🏽‍♂️')
b2 = KeyboardButton('📍 Расположение')
b3 = KeyboardButton('⏳ Режим работы')
b4 = KeyboardButton('✔️ Условия')
# b4 = KeyboardButton('/Показать где я', request_location = True)
# b5 = KeyboardButton('/ПОделиться номером', request_contact = True)

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client.add(b1).add(b2).add(b3).add(b4)#.add(b5)

#Клавиатура для вкладки "Оборудование"
kb_eq1 = KeyboardButton('🏕️ Туристическое оборудование')
kb_eq2 = KeyboardButton('🏄🏽‍♂️ Сап_борды')
kb_eq3 = KeyboardButton('🔥 Баня-палатка')
kb_eq4 = KeyboardButton('📄 Меню')

kb_client2 = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client2.add(kb_eq1).add(kb_eq2).add(kb_eq3).add(kb_eq4)

#Клавиатура для вкладки "Оборудование"
kb_con1 = KeyboardButton('💵 Оплата')
kb_con2 = KeyboardButton('🕑 Срок аренды')
kb_con3 = KeyboardButton('🔑 Бронь')
kb_con4 = KeyboardButton('🗄 Залог')
kb_con5 = KeyboardButton('🔙 Возврат')
kb_con6 = KeyboardButton('🛒 Наличие')


kb_client3 = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client3.add(kb_con1).insert(kb_con2).add(kb_con3).insert(kb_con4).add(kb_con5).insert(kb_con6)