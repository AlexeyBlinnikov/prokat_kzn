from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import token_for_prokat
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = token_for_prokat.TOKEN) 
dp = Dispatcher(bot, storage=storage)
