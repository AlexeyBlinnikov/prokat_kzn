from aiogram.utils import executor
from create_bot import dp
from data_base import db_at_moment


async def on_startup(_):
	print('Бот вышел в онлайн!')
	db_at_moment.start_db()
	# sqlite_db.sql_start_now()


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates= True, on_startup = on_startup)

