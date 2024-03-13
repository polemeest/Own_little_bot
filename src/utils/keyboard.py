"""
Here are all the buttons
"""

from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           )
from aiogram.utils.keyboard import InlineKeyboardBuilder



builder = InlineKeyboardBuilder()


hero_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Алатейя Штормвондер"),
    KeyboardButton(text="Аврора Демулен")],
    [KeyboardButton(text="Винсент Лайт"),
    KeyboardButton(text="Мэлириен Молниеносная")],
    [KeyboardButton(text="Чуди Смоукфёр")]
    ], one_time_keyboard=True, resize_keyboard=True
)


menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я здесь в первый раз", callback_data="start"),
    InlineKeyboardButton(text="Сменить своего героя", callback_data="hero_changer")],
    [InlineKeyboardButton(text="Узнать бюджет района", callback_data="buy_tokens"),
    InlineKeyboardButton(text="Узнать новости", callback_data="balance")]
])

                  
actions_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Узнать свои статы", callback_data="generate_text", add="Узнать статы"),
    InlineKeyboardButton(text="Узнать бюджет города", callback_data="generate_image")],
    [InlineKeyboardButton(text="Узнать бюджет района", callback_data="buy_tokens"),
    InlineKeyboardButton(text="Узнать новости", callback_data="balance")]
])

admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Операции с пользователями", callback_data="user_ops"),
     InlineKeyboardButton(text="Операции с героями", callback_data="hero_ops")],
    [InlineKeyboardButton(text="Операции с казной", callback_data="budget_ops"),]
])

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
