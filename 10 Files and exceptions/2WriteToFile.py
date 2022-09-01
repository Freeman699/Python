#10.3
import re


class GuestToTxt():
    '''
    Класс для преобразования введенного имени пользователем, методом input_name,
    и записи его в текстовый файл с названием guests.txt методом save_guests
    '''
    def __init__(self):
        self.guest_name_list = []

    def get_guest_name_list_copy(self):
        list_copy = self.guest_name_list[:]
        return list_copy

    def input_name(self):
        name = input('Please input name: ')
        self.guest_name_list.append(name)
    
    def print_guest_list(self):
        print('Guest list: ', end='')
        for name in self.guest_name_list:
            print(name + ' ', end='')
        print()
    
    def save_guests(self):
        with open('guests.txt', 'a') as file_object:
            while self.guest_name_list:
                name = self.guest_name_list.pop(0)
                file_object.write(name + '\n')
    

test_guest = GuestToTxt()
for i in range(5):
    test_guest.input_name()
test_guest.print_guest_list()
test_guest.save_guests()



print()
#10.4
class GuestBook(GuestToTxt):

    def __init__(self):
        super().__init__()

    def save_messages(self,list_of_messages):
        with open('guest_book.txt', 'a') as file_object:
            for message in list_of_messages:
                formated_message = message + '\n'
                file_object.write(formated_message)
    
    def guest_greetings(self):
        guest_list = self.get_guest_name_list_copy()
        list_of_messages = []
        for guest in guest_list:
            message = f'Hello, {guest}!'
            print(message)
            list_of_messages.append(message)
        self.save_messages(list_of_messages)


new_guest_book = GuestBook()
for i in range(5):
    new_guest_book.input_name()
new_guest_book.guest_greetings()



print()
#10.5
