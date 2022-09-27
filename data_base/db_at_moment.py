import sqlite3
from create_bot import bot

import sqlite3 as sq
from tkinter import INSERT


def start_db():
    global cursor
    base2 = sq.connect('equipment.db')
    cursor = base2.cursor()

    cursor.execute('CREATE TABLE IF NOT EXIST eq_now(price TEXT PRIMARY KEY, 2_1 TEXT, 2_2 TEXT, 3_2 TEXT, 4_2 TEXT, carpet TEXT, blanket TEXT, chair TEXT, table TEXT')
    cursor.commit()


async def add_to_db():
    async with open ('equipment.db') as f:
        cursor.execute('INSERT INTO eq_now VALUES(?, ?, ?, ?, ?, ?, ?, ?)', f)
        cursor.commit()

async def select_db():
    cursor.execute('SELECT * FROM eq_now ').fetchall()
    


# async def select_db1(message):
#     for r in cursor.execute('SELECT * FROM eq_now ').fetchall():
#         await bot.send_photo(message.from_user.id, f'Палатка 1 слой:{r[0]}\n2 слоя: {r[1]}\n Стол: {r[-1]}')
    


async def delete(r):
    cursor.execute('DELETE FROM eq_now WHERE price = ?', r)
    cursor.commit()