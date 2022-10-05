from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler()
async def echo(message: types.Message):
    bad = ['java', 'bitch', 'lox', 'kotlin', 'плохой мальчик', '😂']
    for word in bad:
        if word in message.text.replace(' ', '').lower():
            await bot.send_message(message.chat.id,
                                   f"Не матерись {message.from_user.full_name} "
                                   f"сам ты {word}")
            await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        bot_dice = a.dice.value


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
