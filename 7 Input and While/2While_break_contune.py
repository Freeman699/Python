#7.4
quit_message = 'quit'
input_message = ''

while input_message != quit_message:
    input_message = input('Input new topping: ')
    if input_message == quit_message:
        break
    else:
        print(f'{input_message} successfully add into order list')

print()

#7.5

age = ''

while age != 'quit':
    age = input('Please input your age: ')
    if age == 'quit':
        break
    else:
        age = int(age)
    
    if (age >= 0) and (age < 3):
        print('Ticket cost: free')
    elif age >= 3 and age < 12:
        print('Ticket cost: 5$')
    elif age >= 12:
        print('Ticket cost: 10$')
    else:
        print('Age input error')

print()

#7.6
print('\n1)')
quit_message = 'quit'
input_message = ''

while input_message != quit_message:
    input_message = input('Input new topping: ')
    if input_message == quit_message:
        continue
    else:
        print(f'{input_message} successfully add into order list')


print('\n2)')
input_message = ''
break_flag = False

while break_flag != True:
    input_message = input('Input new topping: ')
    if input_message == quit_message:
        break_flag = True
    else:
        print(f'{input_message} successfully add into order list')


print('\n3)')
input_message = ''

while True:
    input_message = input('Input new topping: ')
    if input_message == quit_message:
        break
    else:
        print(f'{input_message} successfully add into order list')

print()

#7.7
while True:
    print('Inf cycle')