#7.8
sandwich_orders = [
    'Chicken Sandwich',
    'Egg Sandwich',
    'Seafood Sandwich',
    'Roast Beef Sandwich',
    'Grilled Cheese',
    'Ham Sandwich',
    'Nutella Sandwich',
    'Grilled Chicken Sandwich',
    'Meatball Sandwich'
    ]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made {sandwich}')
    finished_sandwiches.append(sandwich)

print('\nThe sandwiches that were made: ' + str(finished_sandwiches))

print()

#7.9
sandwich_orders = [
    'Pastram'
    'Chicken Sandwich',
    'Egg Sandwich',
    'Seafood Sandwich',
    'Roast Beef Sandwich',
    'Grilled Cheese',
    'Ham Sandwich',
    'Pastram',
    'Nutella Sandwich',
    'Grilled Chicken Sandwich',
    'Pastram',
    'Meatball Sandwich'
    ]
finished_sandwiches = []

print('Pastram sandwich is no longer on the menu')
while 'Pastram' in sandwich_orders:
    sandwich_orders.remove('Pastram')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print('\nThe sandwiches that were made: ' + str(finished_sandwiches))

print()

#7.10
responses = {}
polling_active = True

while polling_active:
    name = input('Please input your name: ')
    response = input('Where would you like to spend your vacation?\n')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f'{name.title()} would like to spend vacation in/at/on {response}')