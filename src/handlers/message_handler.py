"""
Handlers for the bot
"""

import logging
import json

from aiogram import Router, F, Bot, types
from aiogram.types import Message
from aiogram.filters import Command

from utils.keyboard import menu_keyboard, hero_keyboard, admin_keyboard



router = Router()


with open("utils/texts.json", "r", encoding="utf-8") as file:
    texts = json.load(file)[0]


@router.message(Command("admin"))
async def admin_handler(msg: Message) -> str:
    logging.info(f"checking admin {msg.from_user.id}")
    if msg.from_user.id == 1122869980:
        await msg.answer("""Добро пожаловать, сударь. Что пожелаете?
                         \n_______________________________________\n""", 
                         reply_markup=admin_keyboard)
    else:
        await msg.answer(texts.get("info").get("not_an_admin"))


@router.message(Command("start"))
async def start_handler(msg: Message) -> str:
    logging.info(f"started conversation with user {msg.from_user.id}")
    await msg.answer(f"""{texts.get('main').get('greeting')}
                     \n_______________________________________\n
                     {texts.get("main").get("menu")}""", 
                     reply_markup=hero_keyboard)
    

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(texts.get("main").get("menu"), reply_markup=menu_keyboard)


@router.message()
async def message_handler(msg: Message) -> str:
    if msg.text in texts.get("heroes"):
        await msg.answer(f"Приветствую, {msg.text}! К сожалению, данный бот еще в разработке :( Но скоро у нас появлятся тамагочи! :)")
    else:
        await msg.answer(f"К сожалению, господин {msg.text}, у нас таких в Равнике не водится. Идите лесом.")



