from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_today_moon_ru
from keyboards.keyboards import all_moons_kb

router: Router = Router()

# старт
@router.message(CommandStart())
async def process_start_commnd(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=all_moons_kb)


# помощь
@router.message(Command(commands=['/help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=all_moons_kb)


# получение сегоднешней луны
@router.message(F.text == LEXICON_RU['today_moon_button'])
async def process_get_today_moon(message: Message):
    date, moon_data = get_today_moon_ru()
    await message.answer(text=date)
    await message.answer(text="\n".join([f'{k}: {v}' for k, v in moon_data.items()]))


print('основные хендлеры подключены')