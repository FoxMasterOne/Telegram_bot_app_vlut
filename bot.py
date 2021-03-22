from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import convert as cn

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберете одно с предложених действий', reply_markup=kb.con_kb)


@dp.message_handler(content_types=['text'])
async def command_kb(message: types.Message):
    stroka = ''
    data = ['USD', 'EUR', 'RUB']
    data1 = ['USD is UA', 'EUR is UA', 'RUB is UA']
    if message.text in data:
        for key, value in cn.nbu()[message.text].items():
            stroka += str(key) + str(value) + '\n'
        await bot.send_message(message.from_user.id, stroka)
    elif message.text == "All":
        for key, value in cn.nbu().items():
            for key1, value1 in value.items():
                stroka += str(key1) + str(value1) + '\n'
            await bot.send_message(message.from_user.id, stroka)
            stroka = ''
    elif message.text in data1:
        await bot.send_message(message.from_user.id, f'Введите сумму {message.text}: ')
        # машына состояний


if __name__ == '__main__':
    executor.start_polling(dp)