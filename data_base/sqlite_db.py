# from os import curdir
from email.mime import message
import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('prokat_sibirka.db')
    cur = base.cursor()
    if base:
        print("Data connect")
    base.execute('CREATE TABLE IF NOT EXISTS equipment(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


# База данных о наличии
def sql_start_now():
    global base2, cur2
    base2 = sq.connect('eq_now.db')
    cur2 = base2.cursor()
    if base2:
        print("Data2 connect")
    base2.execute('CREATE TABLE IF NOT EXISTS now(tent1 TEXT PRIMARY KEY, tent2 TEXT, tent3 TEXT, tent4 TEXT, blanket TEXT, carpet TEXT, chair TEXT, tab Text)')
    base2.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO equipment VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

# Ввод данных о наличии
async def sql_add2_command(state):
    async with state.proxy() as data:
        cur2.execute('INSERT INTO now VALUES (?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base2.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM equipment').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')


async def sql_read2():
    return cur.execute('SELECT * FROM equipment').fetchall()

# Чтение таблица о наличии
async def select_db1(message):
    for r in cur2.execute('SELECT * FROM now').fetchall():
        await bot.send_photo(message.from_user.id, r[0], f'{r[1],r[2], r[3],r[4], r[5],r[6], r[7]}')#, f'Палатка 1 слой:{r[0]}\n2 слоя: {r[1]}\n {r[2]} {r[3]} {r[4]}{r[5]} {r[6]}Стол: {r[7]}')


async def del_sql(data):
    cur.execute('DELETE FROM equipment WHERE name ==?', (data,))
    base.commit()