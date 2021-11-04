#PYTHONIOENCODING=utf-8 python 2Dict_for.py
#6.4
glossary = {
    'Dict': 'структура данных, преднозначена для объединения данных по принципу "Ключ - Значение"',
    'List': 'структура данных, служит для хранения различных данных одного типа',
    'Immutable': 'неизменяемые типы и структуры данных',
    'Mutable': 'изменяемые типы и структуры данных',
    'len()': 'функция, возвращает кол-во элементов списка, переданного в параметрах'
}
glossary['dict.get("key", "return if empty")'] = 'метод позволяющий узнать значение к ключу. Если такого ключа нету - возвращает None\заданный аргумент'
for key, value in glossary.items():
    print(f'{key} - {value}')

print()

#6.5
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'US',
    'Yenisei': 'Russia',
    'Yukon': 'US',
    'Dnieper': 'Ukraine'
    }

for key, value in rivers.items():
    print(f'The {key} runs through {value}')

for river in rivers.keys():
    print(f'River name:{river}')

for country in set(rivers.values()):
    print(f'Country name:{country}')

print()

#6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
respondents = ['jen', 'sarah', 'edward', 'max', 'phil', 'david', 'bobby', 'lucas']

for name in respondents:
    if name in favorite_languages.keys():
        print(f'Thank You {name.title()} for taking part in the survey.')
    else:
        print(f'{name.title()}, would You like to take part in a survey?')
