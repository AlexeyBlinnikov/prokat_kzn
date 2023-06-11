from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_client2, kb_client3
# from data_base import sqlite_db, db_at_moment
from data_base.sqlite_db import sql_read, select_db1
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# start, help
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Добро пожаловать в наш прокат!", reply_markup = kb_client)
		await message.delete()
	except:
		await message.reply("Общение с ботом через лс!Напишите ему 'https://t.me/prokat_kzn_bot'")
#Главное меню
async def command_menu(message : types.Message):
	await bot.send_message(message.from_user.id, "Основное меню ↓", reply_markup = kb_client)
	await message.delete()
#Главное меню
async def kb_menu(message : types.Message):
	await bot.send_message(message.from_user.id, 'Основное меню ↓', reply_markup = kb_client)
#Помощь
async def help_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Если нужна помощь или есть какие-то вопросы, звоните/пишите по номеру 89872600125.\nС радостью ответим на все ваши вопросы.')
	await message.delete()
#Клавиатура Оборудование
async def eq_kb_menu(message : types.Message):
	await bot.send_message(message.from_user.id, "Все наше оборудование здесь ↓", reply_markup = kb_client2)
#Клавиатура Условия
async def condition_kb(message : types.Message):
	await bot.send_message(message.from_user.id, "За любое оборудование необходимо оставить залог,\nВся информация ниже ↓", reply_markup = kb_client3)
#Расположение
async def shop_place(message : types.Message):
	await bot.send_message(message.from_user.id, "Сибирский тракт д. 5\nВывеска 'Спорт и рыбалка'")
	await bot.send_location(message.from_user.id, 55.804552, 49.184280)
#Режим работы
async def shop_time(message : types.Message):
	await bot.send_message(message.from_user.id, "Работаем ежедневно с 9:30 до 19:30\nБез обеда и выходных.")
#Условия
async def conditions(message : types.Message):
	await bot.send_message(message.from_user.id, "Работаем ежедневно с 9:30 до 19:30\nБез обеда и выходных.")



#Ответы на инлайн кнопки Оборудование
#------------------------------------
#Наличие БД
async def eq_avaliable(call:types.CallbackQuery):
	await select_db1(call)
	await call.answer()
# #Палатки ответ
async def price_tent_equipment(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, "🏕️Палатки:\n\n2-x местныe (однослойные)- 200p в сутки\n2-х местные(двухслойные) - 300 р сутки\n3-x -местные(двухслойные, защита от солнца Fresh&Black) - 400 р сутки \n4-ех меcтныe(двухслойные) - 400 р сутки\n4-ех местные с тамбуром - 500 р сутки\n4-ех местные с тамбуром(раздельные комнаты) - 700 р сутки\n\n🎪Шатер - 600 р сутки\n\n🛏️Спальные мешки:\nЛетний - 150 рТеплый(до +3 градусов) - 250 р\n\nТуристический коврик - 50р. в сутки\nСтул(кресло) - 100 р. в сутки\nСтол складной на 4-6 человек(4 стула в комплекте) - 300 р в сутки\nМатрас + насос - 300 р сутки\nКазан + подставка - 300 р сутки \nМангал - 200 р сутки\nШампура(6шт) - 100 р сутки\nКотелок + тренога - 200 р сутки")
	await call.answer()
async def eq_menu(call:types.CallbackQuery):
	await sql_read(call)
	await call.answer()

async def tent_instruction(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, 'Снизу представлены ссылки на видео инструкции по установке палаток', reply_markup = InlineKeyboardMarkup()
					.add(InlineKeyboardButton('Сборка палатки 2-х местной Pavillo', url ='https://www.youtube.com/watch?v=YqXZBqtjDsc'))
					.add(InlineKeyboardButton('Сборка палатки 2-х местной Декатлон', url ='https://www.youtube.com/watch?v=jYi_2GlZCdY'))
					.add(InlineKeyboardButton('Сборка палатки 3-х местной Fresh&Black', url ='https://www.youtube.com/watch?v=XHX4yvSA31Q'))
					.add(InlineKeyboardButton('Сборка палатки 4-х местной Pavillo', url ='https://www.youtube.com/watch?v=fQo3z8XIzPA&t=184s'))
					.add(InlineKeyboardButton('Сборка палатки 4-х местной Apenaz Family 4', url ='https://youtu.be/74hEfIqisWw'))
					.add(InlineKeyboardButton('Сборка палатки 4-х местной Outventure Hudson 4', url ='https://youtube.com/shorts/7t0CWSnFifM?feature=share')))
	await call.answer()

#Сапы ответ
async def price_sup(call:types.CallbackQuery):
	await call.message.answer("💵 Стоимость комплекта:\nБудни:\n500 руб/день\n800 руб/сутки\n\nВыходные(Пятница, Суббота, Воскресенье):\n1000 руб/день\n1300 руб/сутки\n\nСап на выходные(Тариф активен с пятницы 14:00, возврат до понедельника 12:00):\n2000 руб")
	await call.answer()
async def sup_complect(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, '🏄🏽‍♂️ Сап борд \n🧺 Сумка для переноски\n⛽️ Насос ручной с монометром \n🛶 Весло\n📿 Лиш для ноги\n🚣‍♀️ Сиденье и подставка для ног\n📱 Чехол водонепроницаемый для телефона \n🦺 Жилет спасательный')
	await call.answer()
async def sup_size(call:types.CallbackQuery):
	await call.message.answer("Сапы Hydro Force Oceana 10'\nРазмеры: 305х84х15 см")
	await bot.send_photo(call.from_user.id, 'AgACAgIAAxkBAAIDXWNFWE2cMQagTFZHKMuXikRsIrdzAAJJwzEbD4QxSm-yhi5M0j4aAQADAgADcwADKgQ')
	await call.answer()
async def instruction_sup(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, "Убедитесь, что клапан повернут и находится в режиме накачивания. Отмечен красным.")
	await bot.send_photo(call.from_user.id,'AgACAgIAAxkBAAIGeWQtOpQvu-azmYm7GUshGPMMowFbAAJHxDEbs7BpSYw7T3nP7mI9AQADAgADcwADLwQ')
	await bot.send_message(call.from_user.id, 'Если нет, нажмите на него и поверните.\nДалее вставляете насос и накачиваете до 10-12 PSI')
	await call.answer()
async def instruction_sup_out(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, 'Необходимо нажать на клапан, отмеченный красным, и повернуть в другое положение.')
	await bot.send_photo(call.from_user.id,'AgACAgIAAxkBAAIGeWQtOpQvu-azmYm7GUshGPMMowFbAAJHxDEbs7BpSYw7T3nP7mI9AQADAgADcwADLwQ')
	await call.answer()

#Баня палатка ответ
async def sauna_description(call:types.CallbackQuery):
	await bot.send_photo(call.from_user.id, "AgACAgIAAxkBAAIGqmQtP6cU8mUUSK1-L1jGsVjHH7QIAAJXxDEbs7BpSabiBFGVVfq6AQADAgADcwADLwQ")
	await bot.send_photo(call.from_user.id, "AgACAgIAAxkBAAIGtGQtP8wRetrQKImUfW_cECCmDd2ZAAJUxDEbs7BpSZYTzJkn0MU6AQADAgADcwADLwQ")
	await bot.send_message(call.from_user.id, "Трехслойная баня-палатка МОРЖ - это новый уровень походных бань, которая гарантирует вам получить весь спектр удовольствий как от полноценной стационарной бани!\nРазмер ДхШхВ: 200х200х195\nРазмер в сложенном виде ДхШхВ: 55х35х25\nВес, кг: 8.3\n\nБанная печь INTENT:\nРазмер в сложенном виде ДхШхВ: 60х24х57\nВес, кг: 17")
	await call.answer()
async def sauna_set(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, '⛺️ Баня-палатка МОРЖ\n🔥 Печь для мобильной бани INTENT\n🪑 Скамейка\n🏔 Камни для печи')
	await call.answer()
async def sauna_price(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, 'Стоимость за сутки в будние дни:\n1500 руб\n\nВыходные(Пятница, Суббота, Воскресенье) и праздничные дни:\n2000 руб\n\nБаня на выходные(Забираете в пятницу, крайний срок возврата - понедельник до 12:00):\n3900 руб')
	await call.answer()
#Ответы на инлайн кнопки Условия
#-------------------------------



# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('have'))
# async def now(call:types.CallbackQuery):
# 	await bot.send_message(call.from_user.id, 'Свободные сапы на субботу: 15 шт\nCвободные сапы на воскресенье: 15 шт\n')

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('document'))
# async def now(call:types.CallbackQuery):
# 	await bot.send_message(call.from_user.id, 'В залог необходимо оставить любой документ, удостоверяющий личность.\n(Права, паспорт, Снилс и т.д.)\nТакже возможен денежный залог, он рассчитывается индивидуально и эквивалентен сумме взятого в прокат оборудования')

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('document_sup'))
# async def now(call:types.CallbackQuery):
# 	await bot.send_message(call.from_user.id, 'В залог необходимо оставить любой документ, удостоверяющий личность.\n(Права, паспорт, Снилс и т.д.)\nТакже возможен денежный залог в размере 20000 рублей за один Сап Борд')

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('instruction_tent'))


#Обычные кнопки Оборудование
#---------------------------

#Туристическое оборудование
async def equipment_command(message: types.Message):
	await bot.send_message(message.from_user.id, text ='Туристическое оборудование', reply_markup =InlineKeyboardMarkup()
							.add(InlineKeyboardButton('Фото и описание', callback_data = 'eq_menu'))
							.add(InlineKeyboardButton('Стоимость', callback_data = 'price_tent_equipment'))
							.add(InlineKeyboardButton('Инструкция по сборке', callback_data = 'instruction_tent')))
							# .add(InlineKeyboardButton(f'Залог', callback_data = f'document')))

#Сапы
async def sup_board(message : types.Message):
	await bot.send_message(message.from_user.id, text ='Мы сдаем сапы на день/сутки/выходные\nЧто именно вас инетересует?', reply_markup =InlineKeyboardMarkup()
							.add(InlineKeyboardButton('Стоимость', callback_data = 'price_sup'))
							.add(InlineKeyboardButton('Какие сапы сдаем', callback_data = 'sup_size'))
							.insert(InlineKeyboardButton('Что в комплекте', callback_data = 'sup_complect'))
							.add(InlineKeyboardButton('Накачать/давление', callback_data = 'instruction_sup'))
							.insert(InlineKeyboardButton('Как сдувать', callback_data = 'instruction_sup_out'))
							.add(InlineKeyboardButton('Инструкция по использованию', url ='https://www.youtube.com/watch?v=PFuS8QYS2zw')))
							# .add(InlineKeyboardButton(f'Залог', callback_data = f'document_sup')))

#Баня палатка
async def sauna_tent(message: types.Message):
	await bot.send_message(message.from_user.id, text ='Баня_палатка', reply_markup =InlineKeyboardMarkup()
							.add(InlineKeyboardButton('Описание', callback_data = 'sauna_description'))
							.add(InlineKeyboardButton('Комплект', callback_data = 'sauna_set'))
							.add(InlineKeyboardButton('Стоимость', callback_data = 'sauna_price'))
							.add(InlineKeyboardButton('Инструкция по сборке', url ='https://www.youtube.com/watch?v=sx0MbuHtUn4')))


#Обычные кнопки Условия
#---------------------------
async def pay(message : types.Message):
	await bot.send_message(message.from_user.id, "Оплата возможна только наличными, либо переводом.\nПеревод по номеру 89872600125 Алексей Игоревич Б.\nСбербанк|Тинькофф|Альфа")
async def rent_time(message : types.Message):
	await bot.send_message(message.from_user.id, "Условия по прокату туристического оборудования 🏕️:\nЗа сутки аренды мы считаем не 24 часа, а следующий возвратный день. Например, вы берете оборудование в субботу в 10:00 утра, возвращаете в воскресенье в 19:00 - это 1 арендные сутки.\n\nУсловия по прокату Sup-board 🏄🏽‍♂️:\nСутки - 24 часа + 2 часа на дорогу\nДень - берете утром, возвращаете до 19:30 этого же дня")
async def booking(message : types.Message):
	await bot.send_message(message.from_user.id, "Бронируем только по предоплате 50%.\nТуристическое оборудование можно забронировать от 2-ух суток и более, на сутки бронирование не осуществляем, можно забрать только по наличию.\nСапы, баню-палатку можно забронировать на сутки.")
async def pledge(message : types.Message):
	await bot.send_message(message.from_user.id, "В залог необходимо оставить любой документ, удостоверяющий личность.\n(Права, паспорт, Снилс(при предъявлении документа с фото) и т.д.)\nТакже возможен денежный залог, он рассчитывается индивидуально и эквивалентен сумме взятого в прокат оборудования")
async def return_eq(message : types.Message):
	await bot.send_message(message.from_user.id, "Вернуть все оборудование нужно до 19:30, позже, к сожалению, возврат невозможен.\nКак идет подсчет времени аренды, можете узнать, нажав на кнопку 'Срок аренды'")
async def available_eq(message : types.Message):
	await bot.send_message(message.from_user.id, "С понедельника по пятницу 90% оборудования в наличии(кроме праздников).\nВ выходные при хорошей погоде оборудование разбирают, поэтому мы советуем заранее бронировать все необходимое.\n\nАктуальная информация о наличии по телефону 89872600125.")







def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands =['start'])
	dp.register_message_handler(command_menu, commands =['menu'])
	dp.register_message_handler(help_command, commands =['help'])
	dp.register_message_handler(eq_kb_menu, Text(equals = '🏕️ Оборудование 🏄🏽‍♂️'))
	dp.register_message_handler(shop_place, Text(equals = '📍 Расположение'))
	dp.register_message_handler(shop_time, Text(equals = '⏳ Режим работы'))
	dp.register_message_handler(condition_kb, Text(equals = '✔️ Условия'))
	dp.register_message_handler(equipment_command, Text(equals = '🏕️ Туристическое оборудование'))
	dp.register_message_handler(sup_board, Text(equals = '🏄🏽‍♂️ Сап_борды'))
	dp.register_message_handler(sauna_tent, Text(equals = '🔥 Баня-палатка'))
	dp.register_message_handler(kb_menu, Text(equals = '📄 Меню'))
	dp.register_message_handler(pay, Text(equals = '💵 Оплата'))
	dp.register_message_handler(rent_time, Text(equals = '🕑 Срок аренды'))
	dp.register_message_handler(booking, Text(equals = '🔑 Бронь'))
	dp.register_message_handler(pledge, Text(equals = '🗄 Залог'))
	dp.register_message_handler(return_eq, Text(equals = '🔙 Возврат'))
	dp.register_message_handler(available_eq, Text(equals = '🛒 Наличие'))

	dp.register_callback_query_handler(tent_instruction, lambda x: x.data and x.data.startswith('instruction_tent'))
	dp.register_callback_query_handler(eq_menu, Text(equals = 'eq_menu'))
	dp.register_callback_query_handler(eq_avaliable, Text(equals = 'eq_avaliable'))
	dp.register_callback_query_handler(sup_complect, Text(equals = 'sup_complect'))
	dp.register_callback_query_handler(sup_size, Text(equals = 'sup_size'))
	dp.register_callback_query_handler(price_sup, Text(equals = 'price_sup'))
	dp.register_callback_query_handler(instruction_sup, Text(equals = 'instruction_sup'))
	dp.register_callback_query_handler(instruction_sup_out, Text(equals = 'instruction_sup_out'))
	dp.register_callback_query_handler(sauna_description, Text(equals = 'sauna_description'))
	dp.register_callback_query_handler(sauna_set, Text(equals = 'sauna_set'))
	dp.register_callback_query_handler(sauna_price, Text(equals = 'sauna_price'))
	dp.register_callback_query_handler(price_tent_equipment, Text(equals = 'price_tent_equipment'))




