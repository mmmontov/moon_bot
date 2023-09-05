from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_today_moon_ru, get_week_moons_format
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
    moon_data = "\n".join([f'{k}: {v}' for k, v in moon_data.items()])
    await message.answer(text=f'{date}:\n\n{moon_data}')
    # await message.answer(text=)
    
# получение прогноза лун на неделю
@router.message(F.text == LEXICON_RU['week_moons_button'])
async def process_get_week_moons(message: Message):
    await message.answer(text=get_week_moons_format())


print('основные хендлеры подключены')