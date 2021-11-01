#5.8
users = ['Adam', 'Johan', 'Tommy', 'Admin', 'Henry']
for user in users:
    if user.lower() == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again')

print()

#5.9
if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Hello {user.title()}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again')
else:
    print('We need to ind some users!')

print()

#5.10
for iter in range(len(users)):
    name = users.pop(0).lower()
    users.append(name)
print(users)

new_users = ['HENRY', 'Mia', 'Bobby', 'tOmmY']
if users and new_users:
    for new_user in new_users:
        if new_user.lower() in users:
            print(f'User "{new_user}" need to change her\his name')
        else:
            print(f'Name "{new_user}" is available')

print()

#5.11
num_generated_list = [num for num in range(1,11)]
for number in num_generated_list:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')