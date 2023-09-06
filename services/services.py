from parsers.today_moon_parser import get_today_moon, get_today_moon_pic
from parsers.week_moons_parser import get_week_moons


# перевод информации на русский
def get_today_moon_ru():
    ru_moon_data = {}
    ru_property = ['Фаза луны', 'Видимость', 'Восход/Закат', 'Возраст луны', 'Угловой размер луны', 'Расстояние до луны']
    today_date, moon_data = get_today_moon()
    for ru, elem in zip(ru_property, moon_data.values()):
        ru_moon_data[ru] = elem

    return today_date, ru_moon_data


# форматирование информации на неделю
def get_week_moons_format():
    data = get_week_moons()
    format_data = []
    for d, v in data:
        format_data.append(f'{d}:')
        format_data.append("\n".join(v)+'\n')

    return "\n".join(format_data)

def get_today_moon_pick_src():
    return get_today_moon_pic()



print('сервисы подключены')