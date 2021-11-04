#PYTHONIOENCODING=utf-8 python 'fileName.py'
#6.1
people = {
    'first_name': 'Maxim',
    'second_name': 'Yurchenko',
    'city': 'Kyiv'
    }
print(people['first_name'])
print(people['second_name'])
print(people['city'])

print()

#6.2
favorite_number = {
    'Max': 'i',
    'Anton': '7',
    'Sanya': '300',
    'Kiba': '777',
    'Kirill': '8'
}
number = favorite_number['Max']
print(f'My favorite number is {number}')
number = favorite_number['Anton']
print(f'Anton`s favourite number is {number}')
number = favorite_number['Kiba']
print(f'Kiva`s favourite number is {number}')
number = favorite_number['Sanya']
print(f'Sanya`s favourite number is {number}')
number = favorite_number['Kirill']
print(f'Kirill`s favourite number is {number}')

print()

#6.3
glossary = {
    'Dict': 'структура данных, преднозначена для объединения данных по принципу "Ключ - Значение"',
    'List': 'структура данных, служит для хранения различных данных одного типа',
    'Immutable': 'неизменяемые типы и структуры данных',
    'Mutable': 'изменяемые типы и структуры данных',
    'len()': 'функция, возвращает кол-во элементов списка, переданного в параметрах'
}
dict_glossary = glossary['Dict']
list_glossary = glossary['List']
immutable_glossary = glossary['Immutable']
mutable_glossary = glossary['Mutable']
len_glossary = glossary['len()']

print(f'Dict - {dict_glossary}')
print(f'List - {list_glossary}')
print(f'Immutable - {immutable_glossary}')
print(f'Mutable - {mutable_glossary}')
print(f'len() - {len_glossary}')