import config_bot
import text
from bot import dp, bot
from aiogram import types
from aiogram.types.message import ContentType

async def yandex_month(message_chat_id):
    PRICE = types.LabeledPrice(label='Подписка Yandex', amount=12 * 100)
    if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
        await bot.send_message(chat_id=message_chat_id, text='Тестовый платеж')
    await bot.send_invoice(chat_id=message_chat_id,
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
    async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


    @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
    async def successful_payment(message: types.Message):
        print('Successful')
        payment_info = message.successful_payment.to_python()
        for k, v in payment_info.items():
            print(f'{k} = {v}')
        await bot.send_message(chat_id=message_chat_id, 
                            text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
    
    
    #     result = cur.execute(
    #         """SELECT promocode FROM netflix WHERE id = 1 """).fetchall()
    #     result = result[0][0]
    #     await bot.send_message(message.chat.id,
    #                            f'Ваш промокод: {result}')

    #     cur.execute("""DELETE from yandex where id = 1 """)
    #     cur.commit()

    #     cur.execute("""UPDATE yandex 
    #                     SET id = id - 1
    #                     WHERE id > 1""")
    #     cur.commit()

    # if message.text == 'подписка Netflix':
    #     PRICE = types.LabeledPrice(label='Подписка Netflix', amount=10 * 100)
    #     if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
    #         await bot.send_message(message.chat.id, 'Тестовый платеж')

    #     await bot.send_invoice(message.chat.id,
    #                            title='Подписка Netflix',
    #                            description=text.NETFLIX,
    #                            provider_token=config_bot.PAYMENTS_TOKEN,
    #                            currency='rub',
    #                            photo_url='https://clck.ru/344EfA',
    #                            photo_height=1300,
    #                            photo_width=1300,
    #                            photo_size=1300,
    #                            is_flexible=False,
    #                            prices=[PRICE],
    #                            start_parameter='Netflix',
    #                            payload='tets-invoice-payload')

    # # обработчик платежа до того как была совершена покупка
    # @dp.pre_checkout_query_handler(lambda query: True)
    # async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    #     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

    # # # обработчик  успешной покупки
    # @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
    # async def successful_payment(message: types.Message):
    #     print('Successful')
    #     payment_info = message.successful_payment.to_python()
    #     for k, v in payment_info.items():
    #         print(f'{k} = {v}')
    #     await bot.send_message(message.chat.id,
    #                            f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')

    #     result = cur.execute(
    #         """SELECT promocode FROM netflix WHERE id = 1 """).fetchall()
    #     result = result[0][0]
    #     await bot.send_message(message.chat.id,
    #                            f'Ваш промокод: {result}')

    #     result = """DELETE from netflix where id = 1 """
    #     cur.commit()

    #     cur.execute("""UPDATE netflix
    #                     SET id = id - 1
    #                     WHERE id > 1""")
    #     cur.commit()