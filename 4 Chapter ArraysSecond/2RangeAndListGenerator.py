numbers_20 = []
for value in range(1,21):
    numbers_20.append(value)
print(numbers_20)

one_million_array = []
for value in range (1, 1000000 + 1):
    one_million_array.append(value)
print(min(one_million_array))
print(max(one_million_array))
print(sum(one_million_array))

even_numbers = []
for value in range (1, 21, 2):
    even_numbers.append(value)
print(even_numbers)

mod_three_numbers = []
for value in range (1,11):
    mod_three_numbers.append(value*3)
print(mod_three_numbers)

сubic_numbers = []
for value in range (1,11):
    сubic_numbers.append(value**3)
print(сubic_numbers)

generator_cubic_numbers = [x**3 for x in range(1,11)]
print(generator_cubic_numbers)