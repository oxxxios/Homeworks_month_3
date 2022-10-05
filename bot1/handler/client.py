from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot
from Keyboards import client_kb
from database.bot_db import sql_command_random
from parser import news


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салалекум хозяин {message.from_user.full_name}",
                           reply_markup=client_kb.start_markup)


# @dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"ЭТО ТЕКСТ САМ РАЗБИРАЙСЯ",
                           reply_markup=client_kb.hi_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "За сколько хочешь меня купить?! АА!? "
    answers = [
        '15к сомов', "10 сомов", "Бесплатно", "Бесценно"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Размечтался Не продаюсь",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def show_random_user(message: types.Message):
    await sql_command_random(message)


async def parser_news(message: types.Message):
    data = news.parser()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f"{item['title']}\n\n"
            f"{item['Companytitle']}\n"
            f"{item['upper']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(show_random_user, commands=['random'])
    dp.register_message_handler(parser_news, commands=['news'])