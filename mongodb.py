from pymongo import MongoClient
from datetime import datetime, date


cluster = MongoClient(
    "mongodb+srv://ever:2WZrFserIVEAUKtv@cluster0.qz7oass.mongodb.net/")


async def user_transaction(user_id, item):
    db = cluster['User_histiry']
    collection = db['Transaction']
    existing_document = collection.find_one({'_id': user_id})
    if existing_document:
        collection.update_many({'_id': user_id}, {
                               '$set': {'last_transaction': str(datetime.now().date()),
                                        'last_item': item}})
        return 'Значения last_transaction и last_item обновлены '
    else:
        collection.insert_one({
            '_id': user_id,
            'first_transaction': str(datetime.now().date()),
            'last_transaction': str(datetime.now().date()),
            'last_item': item
        })
        return 'Запись пароизошла успешно'


async def yandex_month(user_id):
    try:
        db = cluster['Yandex']
        collection = db['month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Яндекс Плюс 1 месяц')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)

async def yandex_6month(user_id):
    try:
        db = cluster['Yandex']
        collection = db['6month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Яндекс Плюс 6 месяцев')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)

async def yandex_12month(user_id):
    try:
        db = cluster['Yandex']
        collection = db['12month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Яндекс Плюс 12 месяцев')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)


async def Netflix_month(user_id):
    try:
        db = cluster['Netflix']
        collection = db['month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Netflix 1 месяц')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)


async def Netflix_6month(user_id):
    try:
        db = cluster['Netflix']
        collection = db['6month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Netflix 6 месяцев')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)


async def Netflix_12month(user_id):
    try:
        db = cluster['Netflix']
        collection = db['12month']
        promo_code = collection.find_one({'_id': 1})
        if promo_code:
            promocode = promo_code.copy()
            collection.delete_one({'id': 1})
            collection.update_many({}, {'$inc': {'id': -1}})
            print('Промокод с ID 1 удален и остальные ID обновлены')
            await user_transaction(user_id, 'Netflix 12 месяцев')
            return promocode
        else:
            return {'promo':'Промокод не удалось отправить'}
    except Exception as e:
        print(e)
