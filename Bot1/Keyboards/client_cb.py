from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("Share location", request_location=True)
info_button = KeyboardButton("Share info", request_contact=True)


start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(start_button, help_button, quiz_button)
start_markup.add(location_button, info_button)


hi_button = KeyboardButton("/hi")
hi_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
hi_markup.add(hi_button)

gender_g = KeyboardButton("Я девушка")
gender_b = KeyboardButton("Я парень")
gender_other = KeyboardButton("Я незнаю")
gender_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
gender_markup.row(gender_b, gender_g, gender_other)

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(cancel_button)