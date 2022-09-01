# 9.1
class Restaurant():
    """Простая модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация аргументов restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Простое описание ресторана"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is open")


restaurant = Restaurant("ratatouille", 'Franch')
print(f"Name: {restaurant.restaurant_name}\t Curisine type: {restaurant.cuisine_type}")
restaurant.open_restaurant()
restaurant.describe_restaurant()



print()
#9.2
new_restaurant  = Restaurant('new ratouille', 'Franch')
la_restaurant   = Restaurant('MGM restaurant', 'American')
giga_restaurant = Restaurant('Chad restaurant', 'cheddar')

list_of_restaurants = [
                new_restaurant,
                la_restaurant,
                giga_restaurant
                ]

for element in list_of_restaurants:
    element.describe_restaurant()



print()
# 9.3
class User():
    """Простой класс пользователя"""

    def __init__(self, first_name, last_name, age, gender = None):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f'First name: {self.first_name.title()}')
        print(f'Last name : {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
    
    def greet_user(self):
        print(f'Good day, {self.first_name.title()} {self.last_name.title()}')


user_1 = User('Max', 'Yurchenko', '22', 'male',)
user_2 = User('Ann', 'Holl', '27', 'female')
user_3 = User('Anon', 'anon', '0')

users_data = [
            user_1,
            user_2,
            user_3
            ]

for user in users_data:
    user.describe_user()
    user.greet_user()
    print()