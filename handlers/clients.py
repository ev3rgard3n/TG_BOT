from bot import dp, bot
from aiogram import types
from keyboards import keyboards
from aiogram.types.message import ContentType
import text
import config_bot
import mongodb


async def start(message: types.Message):
    try:
        await message.answer(
            f"""🤖Привет, <b>{message.from_user.username}</b>! Рад сообщить, что ты попал в магазин самых низких цен на подписки Seller Project🤖.\nРассказать почему Seller Project - лучший магазин подписок?""",
            parse_mode='HTML', reply_markup=keyboards.mainmenu)
        await message.delete()

    except Exception as e:
        print(e)


async def all_keyboards(message: types.Message):
    try:
        a = message.chat.id
        match message.text:
            case "Расскажи!":
                await bot.send_message(chat_id=message.chat.id, text=f'1. Самые низкие цены в мире\n2. Более 1000 положительнных отзывов\n3. Промокод на подписку можно активировать на любом аккаунте', reply_markup=keyboards.yandex_netflix)
            case  "Магазин":
                await bot.send_message(chat_id=message.chat.id, text='Хотите приобрести Яндекс Плюс или Netflix?', reply_markup=keyboards.yandex_netflix)
            case "Яндекс Плюс":
                await bot.send_photo(chat_id=message.chat.id, caption=text.YANDEX, photo='https://clck.ru/344DiK', reply_markup=keyboards.yandex_all)
            case "Netflix":
                await bot.send_photo(chat_id=message.chat.id, caption=text.NETFLIX, photo='https://clck.ru/344EfA', reply_markup=keyboards.netflix_all)
            case _:
                await bot.send_message(chat_id=message.chat.id, text='Я не понял, что ты хочешь от меня')
    except Exception as e:
        print(e)


async def inline_yandex(call: types.CallbackQuery):
    try:
        user_id = call.message.chat.id
        match call.data:
            case "yandex_month":
                PRICE = types.LabeledPrice(label='Подписка Yandex', amount=12 * 1000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Яндекс Плюс 1 месяц',
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


                @dp.pre_checkout_query_handler(lambda query: True)
                async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
                    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


                @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
                async def successful_payment(message: types.Message):
                    print('Successful')
                    payment_info = message.successful_payment.to_python()
                    for k, v in payment_info.items():
                        print(f'{k} = {v}')
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    
                    result = await mongodb.yandex_month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])
            
            case "yandex_6month":
                PRICE = types.LabeledPrice(label='Подписка Yandex', amount=38 * 1000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Яндекс Плюс на 6 месяцев',
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

                @dp.pre_checkout_query_handler(lambda query: True)
                async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
                    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


                @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
                async def successful_payment(message: types.Message):
                    print('Successful')
                    payment_info = message.successful_payment.to_python()
                    for k, v in payment_info.items():
                        print(f'{k} = {v}')
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    result = await mongodb.yandex_6month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])

            case "yandex_12month":
                PRICE = types.LabeledPrice(label='Подписка Yandex', amount=12 * 10000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Яндекс Плюс на 12 месяцев',
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
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    result = await mongodb.yandex_12month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])
            
            case _:
                pass
    except Exception as e:
        print(e)


async def inline_netflix(call: types.CallbackQuery):
    try:
        user_id = call.message.chat.id
        match call.data:
            case "netflix_month":
                PRICE = types.LabeledPrice(label='Подписка Yandex', amount=12 * 1000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Netflix 1 месяц',
                                        description=text.NETFLIX,
                                        provider_token=config_bot.PAYMENTS_TOKEN,
                                        currency='rub',
                                        photo_url='https://clck.ru/344DiK',
                                        photo_height=1300,
                                        photo_width=1300,
                                        photo_size=1300,
                                        is_flexible=False,
                                        prices=[PRICE],
                                        start_parameter='Netflix',
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
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    result = await mongodb.Netflix_month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])
            
            case "netflix_6month":
                PRICE = types.LabeledPrice(label='Подписка Netflix', amount=38 * 1000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Netflix на 6 месяцев',
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
                async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
                    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


                @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
                async def successful_payment(message: types.Message):
                    print('Successful')
                    payment_info = message.successful_payment.to_python()
                    for k, v in payment_info.items():
                        print(f'{k} = {v}')
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    result = await mongodb.Netflix_6month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])
            
            case "netflix_12month":
                PRICE = types.LabeledPrice(label='Подписка Netflix', amount=12 * 10000)
                if config_bot.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
                    await bot.send_message(chat_id=call.message.chat.id, text='Тестовый платеж')
                await bot.send_invoice(chat_id=call.message.chat.id,
                                        title='Подписка Netflix на 12 месяцев',
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
                async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
                    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


                @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
                async def successful_payment(message: types.Message):
                    print('Successful')
                    payment_info = message.successful_payment.to_python()
                    for k, v in payment_info.items():
                        print(f'{k} = {v}')
                    await bot.send_message(chat_id=call.message.chat.id, 
                                        text=f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
                    result = await mongodb.Netflix_12month(user_id)
                    await bot.send_message(chat_id=call.message.chat.id, text=result['promo'])
            
            case _:
                pass
    except Exception as e:
        print(e)


def register_client_handler():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(all_keyboards, state=None)
    dp.register_callback_query_handler(inline_yandex, state=None)
    dp.register_callback_query_handler(inline_netflix, state=None)
