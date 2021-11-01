#5.3
print('#1')
alien_color = 'red'
if alien_color == 'green':
    print('+5 score points')

print('#2')
alien_color = 'green'
if alien_color == 'green':
    print('+5 score points')

print()

#5.4
print('#1')
alien_color = 'green'
if alien_color == 'green':
    print('+5 score points')
else:
    print('+10 score points')

print('#2')    
alien_color = 'red'
if alien_color == 'green':
    print('+5 score points')
else:
    print('+10 score points')

print()

#5.5
print('#1')
alien_color = 'green'
if alien_color == 'green':
    print('+5 score points')
elif alien_color == 'yellow':
    print('+10 score points')
elif alien_color == 'red':
    print('+15 score points')

print('#2')
alien_color = 'yellow'
if alien_color == 'green':
    print('+5 score points')
elif alien_color == 'yellow':
    print('+10 score points')
elif alien_color == 'red':
    print('+15 score points')

print('#3')
alien_color = 'red'
if alien_color == 'green':
    print('+5 score points')
elif alien_color == 'yellow':
    print('+10 score points')
elif alien_color == 'red':
    print('+15 score points')

print('#4')
alien_color = 'blue'
if alien_color == 'green':
    print('+5 score points')
elif alien_color == 'yellow':
    print('+10 score points')
elif alien_color == 'red':
    print('+15 score points')

print()

#5.6
age = 64

if   age < 2:
    print('baby')
elif age < 4:
    print('child')
elif age < 13:
    print('kid')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('old')

print()

#5.7
favorite_fruits = ['bananas', 'apples', 'grape']

if 'bananas' in favorite_fruits:
    print('I really like bananas!')
if 'coconuts' in favorite_fruits:
    print('I really like coconuts!')
if 'grape' in favorite_fruits:
    print('I really like grape!')
if 'apples' in favorite_fruits:
    print('I really like apples!')
if 'oranges' in favorite_fruits:
    print('I really like oranges!')
    