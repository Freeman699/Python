#10.11
print('\n\n\n\n\t////#10.11////')
import json
from sre_constants import BRANCH

def input_number_func():
    '''Запрашивает любимое число пользователя'''
    try:
        temp = input('Please enter your favourite number: ')
        f_num = float(temp)
    except ValueError:
        print(f'Error, {temp} is not a number, cannot convert, exiting.')
        exit(0)
    return f_num

def save_number_func(file_name, num):
    '''Создает файл JSON и сохраняет в нём любимое число пользователя'''
    with open(file_name, 'w') as f:
        json.dump(num, f)

def save_favourite_number():
    '''
    Запрашивает любимое число пользователя, 
    сохраняет его и сообщает об успешном выполнении
    '''
    number = input_number_func()
    file_name = 'FavNum.json'
    save_number_func(file_name, number)
    print('Number saved successfully!')

def read_number_func(file_name):
    '''
        Считывает и возвращает число из файла.
    '''
    try:
        with open(file_name) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def read_favourite_number():
    '''
    Выводит сообщение с любимым числом пользователя.
    '''
    file_name = 'FavNum.json'
    num = read_number_func(file_name)
    print(f'I know your favourite number! It is: {num}')
    

save_favourite_number()
read_favourite_number()



#10.12
print('\n\n\n\n\t////#10.12////')

class FavNum():
    '''
    Класс позволяющий сохранять и выводить любимое число пользователя
    '''

    def save_num(self,number):
        '''Создает файл JSON и сохраняет в нём любимое число пользователя'''
        with open(self.filename, 'w') as f:
            json.dump(number, f)


    def input_num(self):
        try:
                temp = input('Please enter your favourite number: ')
                fnum = float(temp)
        except ValueError:
                print(f'Error, {temp} is not a number, cannot convert, exiting.')
                exit(0)

        self.save_num(fnum)
    
        return fnum

    def favourite_number_func(self):
        '''
        Функция для получения любимого числа
        Если находит файл с любимым числом -> возвращает число из файла
        Если файла не найдено создает файл и запрашивает число у пользователя
        '''

        try:
            with open(self.filename) as f:
                fnum = json.load(f)
        except:
                fnum = self.input_num()

        return fnum
                

    def __init__(self):
        self.filename = 'PersNum.json'
        self.favourite_number = self.favourite_number_func()

    def print_fav_num(self):
        print(f'Your favourite number is: {self.favourite_number}')


my_numer = FavNum()
my_numer.print_fav_num()



#10.13
print('\n\n\n\n\t////#10.13////')


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        while True:
            answer = input(f'{username}, is it your username?\t Y/N >>>')
            if answer.lower() == 'y':
                print(f"Welcome back, {username}!")
                break
            elif answer.lower() == 'y':
                username = get_new_username()
                print(f"We'll remember you when you come back, {username}!")
                break
            else:
                print('Something went wrong, please retry!')
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()