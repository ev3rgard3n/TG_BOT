from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config_bot

storage = MemoryStorage()

bot = Bot(token=config_bot.TOKEN)
dp = Dispatcher(bot, storage=storage)
