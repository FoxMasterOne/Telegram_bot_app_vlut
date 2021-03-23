from aiogram.dispatcher.filters.state import StatesGroup, State


class CnvertStatus(StatesGroup):
    USD_IS_UA = State()
    EUR_IS_UA = State()
    RUB_IS_UA = State()