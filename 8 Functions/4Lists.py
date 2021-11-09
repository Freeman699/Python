#8.9
messages_list = ['first', 'second', 'third', 'fourth']

def show_message(list_of_messages):
    for message in list_of_messages:
        print(message)

show_message(messages_list)

print()

#8.10
new_message_list = []

def show_message(list_of_messages, new_list):
    while list_of_messages:
        message = list_of_messages.pop(0)
        print(message)
        new_list.append(message)

show_message(messages_list, new_message_list)
print(new_message_list)

print()

#8.11
messages_list = ['first', 'second', 'third', 'fourth']
new_message_list = []

def show_message(list_of_messages, new_list):
    while list_of_messages:
        message = list_of_messages.pop(0)
        print(message)
        new_list.append(message)

show_message(messages_list[:], new_message_list)
print(messages_list)
print(new_message_list)