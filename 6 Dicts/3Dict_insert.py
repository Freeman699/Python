#6.7
freeman = {
    'first_name': 'maxim',
    'second_name': 'yurchenko',
    'city': 'kyiv'
    }
letun4ik = {
    'first_name': 'anton',
    'second_name': 'troshanivskey',
    'city': 'kyiv'
}
lenin = {
    'first_name': 'vladimir',
    'second_name': 'ulyanov',
    'city': 'ulyanovsk'
}

people = [freeman, letun4ik, lenin]

for person in people:
    for key, value in person.items():
        print(f'{key}: {value.title()}')
    print()

print()

#6.8
dendi = {
    'kind': 'dog',
    'breed': 'french bulldog',
    'ovner': 'yurchenko maxim'
}
molya = {
    'kind': 'cat',
    'breed': 'none',
    'ovner': 'ilya tserin'
}
friday = {
    'kind': 'ball',
    'breed': '?',
    'ovner': 'robinson crusoe'
}
pets = [dendi, molya, friday]

for pet in pets:
    for key, value in pet.items():
        print(f'{key.title()}: {value.title()}')
    print()

print()

#6.9
favourite_places = {
    'kyiv': ['anton', 'kirill', 'slidan'],
    'lviv': ['maxim', 'anton', 'slidan'],
    'istanbul': ['maxim', 'erdogan']
}

for place, names in favourite_places.items():
    print(f'\n{place.title()} is a favorite city for:')
    for name in names:
        print(name.title() + ' ')

print()

#6.10
favorite_numbers = {
    'Max':   ['i', 'e', 'tau'],
    'Anton': ['7', '160', '2000'],
    'Sanya': ['300', '228', '1337'],
    'Kiba':  ['777', '666', '0'],
    'Kirill':['8', '-200', '3']
}

for name, numbers in favorite_numbers.items():
    print(f'\nFor {name.title()} favorite numbers are:')
    for number in numbers:
        print(number + ' ')

print()

#6.11
citys = {
    'berlin': {
        'country': 'German',
        'population': '3.8 million',
        'fact': 'The Berlin Wall fell on 9 November 1989'
    },
    'istanbul': {
        'country': 'Turkey',
        'popularion': '15 million',
        'fact': 'Before being captured by the Ottomans, the city was called Constantinople'
    },
    'seoul': {
        'country': 'South Korea',
        'popuulation': '9.7 million',
        'fact': 'An evil chubby lives in the north'
    }
}

for city_name, data, in citys.items():
    print(f'\nCity name: {city_name.title()} \nInformation about the city:')
    for data_title, info in data.items():
        print(f'\t{data_title.title()}: {info}')