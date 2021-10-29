#4.10
generated_list = [value for value in range(51)]
print(generated_list)
print(f"\nThe irst three items in the list are: {generated_list[:3]}")
print(f"Three items from the middle of the list are: {generated_list[25:28]}")
print(f"The last three items in the list are: {generated_list[-3:]}")

#4.11
my_pizzas = ["Mozzarella", "Hawaiian", "Diablo"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("4 Cheese")
friend_pizzas.append("Carbonara")
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)