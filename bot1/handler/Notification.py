import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="Но проблема")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Крутые питонщики спят в такое время")


async def dead():
    video = open("media/ztesr.png", "rb")
    await bot.send_video(chat_id=chat_id, video=video, caption="Докер опять сломася,иди работай!")

async def Work():
    video = open("media/zzz.jpg", "rb")
    await bot.send_video(chat_id=chat_id, video=video, caption="Не поверишь,у тебя сегодня работа и завтра работа и даже послезавтра!")



async def scheduler():
    aioschedule.every().day.at("23:00").do(go_to_sleep)
    aioschedule.every().monday.at("8:00").do(dead)
    aioschedule.every().hour.at("10").do(dead)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'я сейчас помру' in word.text)