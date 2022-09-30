

from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db, db_at_moment
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.message_handler(commands = ['start','help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Добро пожаловать в наш прокат!", reply_markup = kb_client)
		await message.delete()
	except:
		await message.reply("Общение с ботом через лс!Напишите ему 'https://t.me/pizza_for_us_bot'")

# @dp.message_handler(commands = ['Расположение'])
async def pizza_place(message : types.Message):
	
	await bot.send_message(message.from_user.id, "Сибирский тракт д. 5\nВывеска 'Спорт и рыбалка'")
	await bot.send_location(message.from_user.id, 55.804552, 49.184280)

# @dp.message_handler(commands = ['Режим работы'])
async def pizza_time(message : types.Message):
	
	await bot.send_message(message.from_user.id, "Работаем ежедневно с 9:30 до 19:30")


#кулбэки ловим инлайн кнопки
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('eq_menu'))
async def eq_menu(call:types.CallbackQuery):
	await sqlite_db.sql_read(call)
	# await call.answer(call.message, 'hi')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('now_at_moment'))
async def now(call:types.CallbackQuery):
	await sqlite_db.select_db1(call)
	
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('complect'))
async def now(call:types.CallbackQuery):
	await bot.send_message(call.from_user.id, 'Сап борд \nСумка для переноски\nНасос ручной с монометром \nВесло\nЛиш для ноги\nСиденье и подставка для ног\nЧехол водонепроницаемый для телефона \nЖилет спасательный')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('size'))
async def now(call:types.CallbackQuery):
	await call.message.answer("Сапы Hydro Force Oceana 10'\nРазмеры: 305х84х15 см")
	# await bot.send_photo(call.from_user.id, 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fmegadecha.pl%2Fua%2Fdeska-sup-board-hydro-force-oceana-xl-combo-10-siedzisko-wioslo-2w1-smycz-p2806&psig=AOvVaw3zQPLbOYvX0YmHoJn4inHX&ust=1664614319638000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCLjS4N-RvPoCFQAAAAAdAAAAABAD')











# @dp.message_handler(commands = ['Сапы'])
async def sup_board(message : types.Message):
	await bot.send_message(message.from_user.id, text ='Мы сдаем сапы на день/сутки/выходные\nЧто именно вас инетересует?', reply_markup =InlineKeyboardMarkup()
							.add(InlineKeyboardButton(f'Наличие на выходные', callback_data = f'have '))
							.add(InlineKeyboardButton(f'Какие сапы мы сдаем', callback_data = f'size '))
							.add(InlineKeyboardButton(f'Что в комплекте', callback_data = f'complect'))
							.add(InlineKeyboardButton(f'Инструкция по использованию', url ='https://www.youtube.com/watch?v=PFuS8QYS2zw')))


async def equipment_command(message: types.Message):
	await bot.send_message(message.from_user.id, text ='Туристическое оборудование', reply_markup =InlineKeyboardMarkup()
							.add(InlineKeyboardButton(f'Оборудование', callback_data = f'eq_menu'))
							.add(InlineKeyboardButton(f'В наличии сейчас', callback_data = f'now_at_moment'))
							.add(InlineKeyboardButton(f'Инструкция по сборке', callback_data = f'instruction')))
							# .add(InlineKeyboardButton(f'Отличие палаток и их размеры', callback_data = f'save ')))








#Обработка текста
#@dp.message_handler(lambda message: 'договор' in message.text)
# async def text_1(message: types.Message):
#     await message.answer('В целях экономии вышего времени - договор не составляем, необходим лишь документ для залога и ваш контактный номер для связи!')

# async def text_2(message: types.Message):
#     await message.answer('Матрасы мы, к сожалению, не сдаем.')
# async def text_3(message: types.Message):
#     await message.answer('Топоры мы, к сожалению, не сдаем.')
# async def text_4(message: types.Message):
#     await message.answer('Казан мы,к сожалению, не сдаем.')


# async def text_5(message: types.Message):
#     await message.answer('Если у вас что-то случилось с оборудованием - ничего страшного, расскажите нам о проблеме и мы сообща решим ее, в большинстве случаев идем на компромисс и не штрафуем/берем минимальную плату, либо рассматриваем альтернативные варианты, которые выгодны для вас.')

# async def text_6(message: types.Message):
#     await message.answer('Введи ниже команду /Наличие и узнаешь сколько сейчас осталось палаток и другого оборудования.\nВсего около 40 палаток\nОбычно в хорошую погоду с пн-пт(обед) в наличии есть все оборудование, пт с обеда до  сб обеда в наличии 50% оборудования, сб с обеда до вечера в наличии 0-20% оборудования')

# async def text_7(message: types.Message):
#     await message.answer('К сожалению работаем ровно с 9:30 до 19:30, сдавать и забирать можно только в это время')
# async def text_8(message: types.Message):
#     await message.answer('Все размеры и все наше оборудование можете посмотреть в разделе "Оборудование" или просто напиши ниже /Оборудование')
# async def text_9(message: types.Message):
#     await message.answer('Мы не продаем наше оборудование/nБольшая часть нашего оборудования из ныне закрытого магазина ДЕКАТЛОН')
# async def text_10(message: types.Message):
#     await message.answer('Если нужна помощь или есть какие-то вопросы, звоните по номеру 89872600125')






def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands =['start', 'help'])
	dp.register_message_handler(pizza_place, commands = ['Расположение'])
	dp.register_message_handler(pizza_time, commands =['Режим_работы'])
	dp.register_message_handler(equipment_command, commands =['Туристическое_оборудование'])
	dp.register_message_handler(sup_board, commands =['Сапы'])
	# dp.register_message_handler(text_1, lambda message: 'привет' in message.text)
	# dp.register_message_handler(text_2, lambda message: 'у тебя' in message.text)
	# dp.register_message_handler(text_3, lambda message: 'ты что' in message.text)
	# dp.register_message_handler(text_4, lambda message: 'да' in message.text)
	# dp.register_message_handler(text_5, Text(equals = 'сломал', ignore_case = True))
	# dp.register_message_handler(text_5) #(lambda message: 'сломал' in message.text or 'потерял' or 'порвал' in message.text), ignore_case = True)
	# dp.register_message_handler(text_6, lambda message: 'наличие' in message.text or 'наличии' in message.text)
	# dp.register_message_handler(text_7, lambda message: 'опаздыва' in message.text or 'позже' in message.text or 'не успева' in message.text)
	# dp.register_message_handler(text_8, lambda message: 'размеры' in message.text)
	# dp.register_message_handler(text_9, lambda message: 'знает' in message.text)
	# dp.register_message_handler(text_10, lambda message: 'снов' in message.text)

