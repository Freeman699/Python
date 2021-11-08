#7.1
car = input('What brand of car would you like to buy?\n')
print(f'Let me see if I can find you a {car}')

print()

#7.2
num_of_people = input('How many seats would you like to book a table for?\n')
num_of_people = int(num_of_people)

if num_of_people >= 8:
    print('Sorry you have to wait for a table')
elif num_of_people > 0:
    print('Your table is ready')
else:
    print('Input error')

print()

#7.3
number = input('Input your number: ')
number = int(number)

if number % 10 == 0:
    print('Your number is evenly divisible by 10')
else:
    print('Your number is not even divisible by 10')