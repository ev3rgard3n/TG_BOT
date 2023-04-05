import sqlite3
import config_bot
import text
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove # import кнопок



# sql
cur = sqlite3.connect('promocode.db')
cursor = cur.cursor()


async def on_startup(_):
    print('Бот запущен!')


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config_bot.TOKEN)
dp = Dispatcher(bot)
#кнопки в боте
kb = [
    [types.KeyboardButton(text="Давай")],
    [types.KeyboardButton(text="подписка Yandex")],
    [types.KeyboardButton(text="подписка Netflix")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

kb1 = [
    [types.KeyboardButton(text="Вау")],
    [types.KeyboardButton(text="подписка Yandex")],
    [types.KeyboardButton(text="подписка Netflix")]
]
keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)

kb2 = [
    [types.KeyboardButton(text="подписка Yandex")],
    [types.KeyboardButton(text="подписка Netflix")]
]
keyboard2 = types.ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)

# обработчик команды start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"""🤖Привет, <b>{message.from_user.username}</b>! Рад сообщить, что вы попали в магазин с самыми низкими ценами на подписки Seller Project🤖. Рассказать почему Seller Project - лучший магазин аккаунтов?""",
        parse_mode='HTML', reply_markup=keyboard)
    await message.delete()

# обработчик команды help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text.HELP_COMMAND)
    await message.delete()

# обработчик команды сообщений
@dp.message_handler()
async def answer(message: types.Message):
    if message.text == 'Давай':  # message.text.lower() == 'да' or message.text.lower() == 'расскажи' or
        await message.answer(text.ADVANTAGES_ANSWER, reply_markup=keyboard1)
    if message.text == 'Вау':
        await message.answer(
            f'Мы умеем удивлять пользователей. {message.from_user.username}, давайте покажу весь наш ассортимент',
            reply_markup=keyboard2)
        
    # обработчик платежа подписки
    if message.text == 'подписка Yandex':
        PRICE = types.LabeledPrice(label='Подписка Yandex', amount=12 * 100)
        if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
            await bot.send_message(message.chat.id, 'Тестовый платеж')

        await bot.send_invoice(message.chat.id,
                               title='Подписка Yandex',
                               description=text.YANDEX,
                               provider_token=config_bot.PAYMENTS_TOKEN,
                               currency='rub',
                               photo_url='https://clck.ru/344DiK',
                               photo_height=1300,
                               photo_width=1300,
                               photo_size=1300,
                               is_flexible=False,
                               prices=[PRICE],
                               start_parameter='Yandex',
                               payload='tets-invoice-payload')

    # обработчик платежа до того как была совершена покупка
    @dp.pre_checkout_query_handler(lambda query: True)
    async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

    # обработчик  успешной покупки
    @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
    async def successful_payment(message: types.Message):
        print('Successful')
        payment_info = message.successful_payment.to_python()
        for k, v in payment_info.items():
            print(f'{k} = {v}')
        await bot.send_message(message.chat.id,
                               f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')

        result = cur.execute(
            """SELECT promocode FROM netflix WHERE id = 1 """).fetchall()
        result = result[0][0]
        await bot.send_message(message.chat.id,
                               f'Ваш промокод: {result}')

        cur.execute("""DELETE from yandex where id = 1 """)
        cur.commit()

        cur.execute("""UPDATE yandex 
                        SET id = id - 1
                        WHERE id > 1""")
        cur.commit()

    if message.text == 'подписка Netflix':
        PRICE = types.LabeledPrice(label='Подписка Netflix', amount=10 * 100)
        if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
            await bot.send_message(message.chat.id, 'Тестовый платеж')

        await bot.send_invoice(message.chat.id,
                               title='Подписка Netflix',
                               description=text.NETFLIX,
                               provider_token=config_bot.PAYMENTS_TOKEN,
                               currency='rub',
                               photo_url='https://clck.ru/344EfA',
                               photo_height=1300,
                               photo_width=1300,
                               photo_size=1300,
                               is_flexible=False,
                               prices=[PRICE],
                               start_parameter='Netflix',
                               payload='tets-invoice-payload')

    # обработчик платежа до того как была совершена покупка
    @dp.pre_checkout_query_handler(lambda query: True)
    async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

    # обработчик  успешной покупки
    @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
    async def successful_payment(message: types.Message):
        print('Successful')
        payment_info = message.successful_payment.to_python()
        for k, v in payment_info.items():
            print(f'{k} = {v}')
        await bot.send_message(message.chat.id,
                               f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')

        result = cur.execute(
            """SELECT promocode FROM netflix WHERE id = 1 """).fetchall()
        result = result[0][0]
        await bot.send_message(message.chat.id,
                               f'Ваш промокод: {result}')

        result = """DELETE from netflix where id = 1 """
        cur.commit()

        cur.execute("""UPDATE netflix
                        SET id = id - 1
                        WHERE id > 1""")
        cur.commit()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
