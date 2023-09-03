from parsers.today_moon_parser import get_today_moon


# перевод информации на русский
def get_today_moon_ru():
    ru_moon_data = {}
    ru_property = ['Фаза луны', 'Видимость', 'Восход/Закат', 'Возраст луны', 'Угловой размер луны', 'Расстояние до луны']
    today_date, moon_data = get_today_moon()
    for ru, elem in zip(ru_property, moon_data.values()):
        ru_moon_data[ru] = elem

    return today_date, ru_moon_data

# print(get_today_moon())
print('сервисы подключены')