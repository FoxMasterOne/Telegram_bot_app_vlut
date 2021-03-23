from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import convert as cn
from utils import CnvertStatus
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберете одно с предложених действий', reply_markup=kb.con_kb)


@dp.message_handler(content_types=['text'], state=None)
async def command_kb(message: types.Message):
    stroka = ''
    data1 = {'USD is UA': CnvertStatus.USD_IS_UA.set(), 'EUR is UA': CnvertStatus.EUR_IS_UA.set(),
             'RUB is UA': CnvertStatus.RUB_IS_UA.set()}
    data = ['USD', 'EUR', 'RUB']
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
        await message.answer(f"Введите сумму{message.text}:")
        await data1[message.text]


@dp.message_handler(state=CnvertStatus.USD_IS_UA)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = int(message.text)
    await message.answer(cn.convert(answer, 'USD'))
    await state.finish()


@dp.message_handler(state=CnvertStatus.EUR_IS_UA)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = int(message.text)
    await message.answer(cn.convert(answer, 'EUR'))
    await state.finish()


@dp.message_handler(state=CnvertStatus.RUB_IS_UA)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = int(message.text)
    await message.answer(cn.convert(answer, 'RUB'))
    await state.finish()


async def on_shutdown():
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)