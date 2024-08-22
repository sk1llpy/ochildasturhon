from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    langauge = State()
    phone_number = State()