from create_bot import bot
# import sqlite3 as sq
import psycopg2 as ps
from tkinter import INSERT

DB_URI = 'postgres://gncxbxpflzktlj:a7631da535f92ffc6742164286b4910b32f4ff1d4d0674c5743abaa310329dd4@ec2-52-207-90-231.compute-1.amazonaws.com:5432/d6prkuu38tt6rq'

def start_db():
    global cursor, base_ps
    base_ps = ps.connect(DB_URI, sslmode = 'require')
    cursor = base_ps.cursor()
    if base_ps:
        print("Data2 connect")

    cursor.execute('CREATE TABLE IF NOT EXISTS prokat(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base_ps.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO prokat VALUES(?, ?, ?, ?)', tuple(data.values()))
        base_ps.commit()

# async def add_to_db():
#     async with open ('equipment.db') as f:
#         cursor.execute('INSERT INTO prokat VALUES(?, ?, ?, ?)', f)
#         cursor.commit()

# async def select_db():
#     cursor.execute('SELECT * FROM eq_now ').fetchall()

async def sql_read(message):
    for ret in cursor.execute('SELECT * FROM prokat').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')


async def sql_read2():
    return cursor.execute('SELECT * FROM prokat').fetchall()
    


# async def select_db1(message):
#     for r in cursor.execute('SELECT * FROM eq_now ').fetchall():
#         await bot.send_photo(message.from_user.id, f'Палатка 1 слой:{r[0]}\n2 слоя: {r[1]}\n Стол: {r[-1]}')
    


# async def delete(r):
#     cursor.execute('DELETE FROM eq_now WHERE price = ?', r)
#     cursor.commit()