from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

get_today_moon_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['today_moon_button'])
get_week_moons_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['week_moons_button'])

all_moons_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[get_today_moon_button], [get_week_moons_button]], resize_keyboard=True)

print('клавиатуры работают')