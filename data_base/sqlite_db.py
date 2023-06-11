# # from os import curdir
# from email.mime import message
import sqlite3 as sq
# import psycopg2 as sq
from create_bot import bot


#_______Создаем бд________
def sql_start():
    global base, cur
    base = sq.connect('prokat_sibirka.db')
    cur = base.cursor()
    if base:
        print("Data connect")
    base.execute('CREATE TABLE IF NOT EXISTS equipment(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()
# База данных о наличии
# def sql_start_now():
#     global base2, cur2
#     base2 = sq.connect('eq_now.db')
#     cur2 = base2.cursor()
#     if base2:
#         print("Data2 connect")
#     base2.execute('CREATE TABLE IF NOT EXISTS now(tent1 TEXT PRIMARY KEY, tent2 TEXT, tent3 TEXT, tent4 TEXT, blanket TEXT, carpet TEXT, chair TEXT, tab Text)')
#     base2.commit()


#________Команда добавления в бд_________
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO equipment VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
# Ввод данных о наличии
# async def sql_add2_command(state):
#     async with state.proxy() as data:
#         cur2.execute('INSERT INTO now VALUES (?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
#         base2.commit()


#__________Читаем данные бд_____________
async def sql_read(message):
    # await bot.send_message(message.from_user.id, 'hi')
    for ret in cur.execute('SELECT * FROM equipment').fetchall():
        # print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')
async def sql_read2():
    return cur.execute('SELECT * FROM equipment').fetchall()
# Чтение таблица о наличии
# async def select_db1(message):
#     await bot.send_message(message.from_user.id, "Информация будет постоянно обновляться с мая 2023, на данный момент не актуальна, уточняйте наличие по телефону")
#     for r in cur2.execute('SELECT * FROM now').fetchall():
#         await bot.send_message(message.from_user.id, f'⛺️ 2 местная 1 слой: {r[0]} шт\n⛺️ 2 местная 2 слоя: {r[1]} шт\n⛺️ 3-ех местная Fresh&Black: {r[2]} шт\n⛺️ 4-ех местная: {r[3]} шт\nСпальные мешки: {r[4]} шт\nКоврики: {r[5]} шт\nСтулья: {r[6]} шт\nСтолы: {r[7]} шт')



#____________Удаляем из бд_____________
async def del_sql(data):
    cur.execute('DELETE FROM equipment WHERE name ==?', (data,))
    base.commit()
# async def del_sql_now():
#     cur2.execute('DELETE FROM now')
#     base2.commit()








# result = []

# def start_db():
#     global cursor, base_ps
#     base_ps = sq.connect(DB_URI, sslmode = 'require')
#     cursor = base_ps.cursor()
#     if base_ps:
#         print("Data1 connect")

# # DB о наличии сапов
# def start_sup():
#     global base, cur
#     base = sq.connect(DB_URI, sslmode = 'require')
#     cur = base.cursor()
#     if base:
#         print("Data2 connect")

#     # cursor.execute('CREATE TABLE IF NOT EXISTS prokat(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
#     # base_ps.commit()


# ДБ оборудование
# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cursor.execute('INSERT INTO prokat VALUES (%s, %s, %s, %s)', tuple(data.values()))
#         base_ps.commit()

# async def sql_read(message):
#     cur.execute('SELECT * FROM equipment')
#     result = cur.fetchall()
#     for ret in result:
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')

# async def sql_read2():
#     cursor.execute('SELECT * FROM prokat')
#     result = cursor.fetchall()
#     return result
    
# async def del_sql(data):
#     print(data)
#     cursor.execute('DELETE FROM prokat WHERE name = %s', (data,))
#     base_ps.commit()

# async def select_db1(message):
#     for r in cursor.execute('SELECT * FROM eq_now ').fetchall():
#         await bot.send_photo(message.from_user.id, f'Палатка 1 слой:{r[0]}\n2 слоя: {r[1]}\n Стол: {r[-1]}')
    

# Дб наличие сапов
# async def sql_add2_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO now VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', tuple(data.values()))
#         base.commit()

# async def select_db1(message):
#     cur.execute('SELECT * FROM now')
#     result = cur.fetchall()
#     for r in result:
#         await bot.send_message(message.from_user.id, f'Палатка 2 местная 1 слой: {r[0]} шт\nПалатка 2 местная 2 слоя: {r[1]} шт\nПалатка 3-ех местная Fresh&Black: {r[2]} шт\nПалатка 4-ех местная: {r[3]} шт\nСпальные мешки: {r[4]} шт\nКоврики: {r[5]} шт\nСтулья: {r[6]} шт\nСтолы: {r[7]} шт')

# async def del_sql_now():
#     cur.execute('DELETE FROM now')
#     base.commit()
