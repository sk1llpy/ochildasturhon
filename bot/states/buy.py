from aiogram.fsm.state import State, StatesGroup

class BuyFoodState(StatesGroup):
    food = State()
    quantity = State()
    location = State()
    confirm = State()