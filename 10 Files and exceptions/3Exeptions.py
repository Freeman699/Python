#10.6 + 10.7
import re


print('\n\n\n\n\t////#10.6 + #10.7////\n')
print("Give me two numbers, and I'll sum them")
print("Enter 'q' to quit.")

while True:
    try:   
        f_val = input('\nFirst value: ')
        if f_val == 'q':
            break
        s_val = input('Second value: ')
        if s_val == 'q':
            break
    except KeyboardInterrupt:
        print("Input error, please try again!")
        continue
    
    try:
        answer = float(f_val) + float(s_val)
    except ValueError:
        print('Invalid data entry, please try again!')
    else:
        print(f'Answer: {answer}')




#10.8
print('\n\n\n\n\t////#10.8////')
class Pets():

    def __init__(self,*file_names):
        self.file_names_list = []
        for name in file_names:
            self.file_names_list.append(name)
    
    def file_read(self,file_name):
        list_of_pet_names = []
        try:
            with open(file_name) as f:
                list_of_pet_names = (f.readlines())
        except FileNotFoundError:
            print(f'File with name {file_name} not found!')
        else:
            return list_of_pet_names
    

my_pets = Pets('dogs.txt', 'cats.txt', 'other.txt')

for file in my_pets.file_names_list:
    print()
    list_of_pet_names = my_pets.file_read(file)
    if list_of_pet_names:
        for name in list_of_pet_names:
            print(f'{name.strip()}')
    else:
        continue



#10.9
print('\n\n\n\n\t////#10.9////')
class PetsSecond():

    def __init__(self,*file_names):
        self.file_names_list = []
        for name in file_names:
            self.file_names_list.append(name)
    
    def file_read(self,file_name):
        list_of_pet_names = []
        try:
            with open(file_name) as f:
                list_of_pet_names = (f.readlines())
        except FileNotFoundError:
            pass
        else:
            return list_of_pet_names
    

my_pets = PetsSecond('dogs.txt', 'cats.txt', 'other.txt')

for file in my_pets.file_names_list:
    print()
    list_of_pet_names = my_pets.file_read(file)
    if list_of_pet_names:
        for name in list_of_pet_names:
            print(f'{name.strip()}')
    else:
        continue



#10.10
print('\n\n\n\n\t////#10.10////')

class WordsCounter():

    def __init__(self, file_names, word):
        self.file_names = file_names
        self.word = word.lower()
    
    def file_open(self, path):
        try:
            with open(path, encoding='utf-8') as f:
                data = f.read()
        except FileNotFoundError:
            print(f'File {path} does not exist.')
            return None
        else:
            return data
    
    def word_cnt(self, text):
        cnt = text.lower().count(self.word)
        return cnt
    
    def count_in_all_files(self):
        for file in self.file_names:
            text = self.file_open(file)
            result = self.word_cnt(text)
            print(f'In the file "{file}" of the words "{self.word}" occurs {result} times')
    

test_word_cnt = WordsCounter(
                ['The_Brothers_Karamazov.txt','Crime_and_Punishment.txt'], 
                'the '
            )
test_word_cnt.count_in_all_files()