from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Наличие онлайн
class FSMAdmin2(StatesGroup):
    tent1 = State()
    tent2 = State()
    tent3 = State()
    tent4 = State()
    blanket = State()
    carpet = State()
    chair = State()
    table = State()


# Получаем id
# @dp.message_handler(commands = ['moderator'], is_chat_admin = True)
async def moderator_or_not(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Валяй', reply_markup = admin_kb.kb_admin)
    await message.delete()

# Начало диалога загрузки меню
# @dp.message_handler(commands = "Загрузить", state = None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')

         #отмена ввода
async def cancel(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return 
        await state.finish()
        await message.reply('Ok')

# Ловим первый ответ
# @dp.message_handler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Введи название')

    # Ловим второй ответ
# @dp.message_handler(state = FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

    # Ловим третий ответ
# @dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену')



    # Ловим четвертый ответ
# @dp.message_handler(state = FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
    # вывод

        await sqlite_db.sql_add_command(state)
        await state.finish()



############################################
# Начало диалога зарузки наличия онлайн

async def cm_start_online(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin2.tent1.set()
        await message.reply('Палатка 2 местная 1 слой')

    # Ловим первый ответ
# @dp.message_handler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_1(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['tent1'] = message.text
        await FSMAdmin2.next()
        await message.reply('Палатка 2 местная 2 слоя')

    # Ловим второй ответ
# @dp.message_handler(state = FSMAdmin.name)
async def load_2(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['tent2'] = message.text
        await FSMAdmin2.next()
        await message.reply('Палатка 3 местная')

    # Ловим третий ответ
# @dp.message_handler(state = FSMAdmin.description)
async def load_3(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['tent3'] = message.text
        await FSMAdmin2.next()
        await message.reply('Палатка 4 местная')

async def load_4(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['tent4'] = message.text
        await FSMAdmin2.next()
        await message.reply('Спальные мешки')

async def load_blanket(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['blanket'] = message.text
        await FSMAdmin2.next()
        await message.reply('Коврики')

async def load_carpet(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['carpet'] = message.text
        await FSMAdmin2.next()
        await message.reply('Стулья')

async def load_chair(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['chair'] = message.text
        await FSMAdmin2.next()
        await message.reply('Столы')


    # Ловим четвертый ответ
# @dp.message_handler(state = FSMAdmin.price)
async def load_table(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['table'] = message.text
    # вывод

        await sqlite_db.sql_add2_command(state)
        await state.finish()

################################################
# конец онлайн ввода




@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def kb_delete(call:types.CallbackQuery):
    await sqlite_db.del_sql(call.data.replace('del ', ''))
    await call.answer(text = f'{call.data.replace("del ", "")} удалена.', show_alert= True)




@dp.message_handler(commands ='удалить')
async def delete_kb(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Описание: {ret[2]}\n Цена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text ='^^^', reply_markup =InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data = f'del {ret[1]}')))
    
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands =['Загрузить'], state = None)
    dp.register_message_handler(cancel, state = "*", commands = ['отмена'])
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case= True), state = "*")
    dp.register_message_handler(load_photo, content_types = ['photo'], state = FSMAdmin.photo)
    dp.register_message_handler(load_name, state = FSMAdmin.name)
    dp.register_message_handler(load_description, state = FSMAdmin.description)
    dp.register_message_handler(load_price, state = FSMAdmin.price)
    dp.register_message_handler(moderator_or_not, commands = ['moderator'], is_chat_admin = True)
    dp.register_message_handler(cm_start_online, commands =['Загрузить_онлайн'], state = None)
    dp.register_message_handler(load_1, state = FSMAdmin2.tent1)
    dp.register_message_handler(load_2, state = FSMAdmin2.tent2)
    dp.register_message_handler(load_3, state = FSMAdmin2.tent3)
    dp.register_message_handler(load_4, state = FSMAdmin2.tent4)
    dp.register_message_handler(load_blanket, state = FSMAdmin2.blanket)
    dp.register_message_handler(load_carpet, state = FSMAdmin2.carpet)
    dp.register_message_handler(load_chair, state = FSMAdmin2.chair)
    dp.register_message_handler(load_table, state = FSMAdmin2.table)