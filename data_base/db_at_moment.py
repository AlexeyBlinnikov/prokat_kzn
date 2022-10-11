from create_bot import bot
# import sqlite3 as sq
import psycopg2 as ps


DB_URI = 'postgres://mhmcqjtxsplozn:0cc84beffbbe8cd1dffab75e10ebf1afd21c0b20a495fdbbf02434ef1d0f31ec@ec2-3-92-98-129.compute-1.amazonaws.com:5432/d821t7d8rkt0uu'
result = []

def start_db():
    global cursor, base_ps
    base_ps = ps.connect(DB_URI, sslmode = 'require')
    cursor = base_ps.cursor()
    if base_ps:
        print("Data1 connect")

# DB о наличии сапов
def start_sup():
    global base, cur
    base = ps.connect(DB_URI, sslmode = 'require')
    cur = base.cursor()
    if base:
        print("Data2 connect")

    # cursor.execute('CREATE TABLE IF NOT EXISTS prokat(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    # base_ps.commit()


# ДБ оборудование
async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO prokat VALUES (%s, %s, %s, %s)', tuple(data.values()))
        base_ps.commit()

async def sql_read(message):
    cursor.execute('SELECT * FROM prokat')
    result = cursor.fetchall()
    for ret in result:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')

async def sql_read2():
    cursor.execute('SELECT * FROM prokat')
    result = cursor.fetchall()
    return result
    
async def del_sql(data):
    print(data)
    cursor.execute('DELETE FROM prokat WHERE name = %s', (data,))
    base_ps.commit()

# async def select_db1(message):
#     for r in cursor.execute('SELECT * FROM eq_now ').fetchall():
#         await bot.send_photo(message.from_user.id, f'Палатка 1 слой:{r[0]}\n2 слоя: {r[1]}\n Стол: {r[-1]}')
    

# Дб наличие сапов
async def sql_add2_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO now VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', tuple(data.values()))
        base.commit()

async def select_db1(message):
    cur.execute('SELECT * FROM now')
    result = cur.fetchall()
    for r in result:
        await bot.send_message(message.from_user.id, f'Палатка 2 местная 1 слой: {r[0]} шт\nПалатка 2 местная 2 слоя: {r[1]} шт\nПалатка 3-ех местная Fresh&Black: {r[2]} шт\nПалатка 4-ех местная: {r[3]} шт\nСпальные мешки: {r[4]} шт\nКоврики: {r[5]} шт\nСтулья: {r[6]} шт\nСтолы: {r[7]} шт')

async def del_sql_now():
    cur.execute('DELETE FROM now')
    base.commit()
