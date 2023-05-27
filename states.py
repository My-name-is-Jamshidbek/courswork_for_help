"""
states
"""
from aiogram.dispatcher.filters.state import State, StatesGroup


class User_state(StatesGroup):
    """
    user all states
    """
    main_menu = State()
    first_menu = State()
