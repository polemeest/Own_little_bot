"""
Handlers for the bot
"""

import logging
import json

from aiogram import Router, F, Bot, types
from aiogram.types import Message
from aiogram.filters import Command

# from utils.keyboard import menu_keyboard, hero_keyboard, admin_keyboard



router = Router()


with open("utils/texts.json", "r", encoding="utf-8") as file:
    texts = json.load(file)[0]



@router.callback_query()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    logging.info(callback_query.inline_message_id)
    await callback_query.answer('Нажата инлайн кнопка!')

