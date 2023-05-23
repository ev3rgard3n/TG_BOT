from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

mainmenu_about = KeyboardButton(text='Расскажи!')
mainmenu_subscribe_button = KeyboardButton(text='Магазин')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).row(mainmenu_about, mainmenu_subscribe_button)

yandex_answer = KeyboardButton(text='Яндекс Плюс')
netflix_answer = KeyboardButton(text='Netflix')
yandex_netflix = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).row(yandex_answer, netflix_answer)

yandex_month = InlineKeyboardButton(text='1 месяц', callback_data='yandex_month') 
yandex_6month = InlineKeyboardButton(text='6 месяцев', callback_data='yandex_6month') 
yandex_12month = InlineKeyboardButton(text='12 месяцев', callback_data='yandex_12month')
yandex_all = InlineKeyboardMarkup(row_width=3).row(yandex_month,yandex_6month,yandex_12month)

netflix_month = InlineKeyboardButton(text='1 месяц', callback_data='netflix_month') 
netflix_6month = InlineKeyboardButton(text='6 месяцев', callback_data='netflix_6month') 
netflix_12month = InlineKeyboardButton(text='12 месяцев', callback_data='netflix_12month')
netflix_all = InlineKeyboardMarkup(row_width=3).row(netflix_month,netflix_6month,netflix_12month)





