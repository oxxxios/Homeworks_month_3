import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="но проблема")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Гуд найт,бот сам себя не напишет!")


async def wake_up():
    video = open("../Media/MFvK4.png", "rb")
    await bot.send_photo(chat_id=chat_id, video=video, caption="Докер опять сломался,иди работай!")


async def scheduler():
    aioschedule.every().day.at("23:00").do(go_to_sleep)
    aioschedule.every().hour.at("13:00").do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'help ,me' in word.text)
