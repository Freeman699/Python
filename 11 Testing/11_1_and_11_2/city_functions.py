def get_formatted_city_name(city, country, population=''):
    '''Форматирует данные в строку вида "Город, Страна"'''
    if population:
        formatted_result = f'{city.title()}, {country.title()} - population: {population}'
    else:
        formatted_result = f'{city.title()}, {country.title()}'
    return formatted_result