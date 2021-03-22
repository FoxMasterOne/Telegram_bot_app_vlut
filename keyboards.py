from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton("USD")
button2 = KeyboardButton("EUR")
button3 = KeyboardButton("RUB")
button4 = KeyboardButton("All")
button5 = KeyboardButton("USD is UA")
button6 = KeyboardButton("EUR is UA")
button7 = KeyboardButton("RUB is UA")
con_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
con_kb.row(button1, button2, button3).add(button4)
con_kb.row(button5, button6, button7)