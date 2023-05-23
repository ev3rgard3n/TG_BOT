from bot import dp, bot
from aiogram.utils import executor
from handlers import clients


async def on_startup(_):
    print('Бот запущен!')


clients.register_client_handler()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
