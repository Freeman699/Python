class Restaurant():
    """Простая модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация аргументов"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Простое описание ресторана"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number



class User():
    """Простой класс пользователя"""

    def __init__(self, first_name, last_name, age, gender = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'First name: {self.first_name.title()}')
        print(f'Last name : {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
    
    def greet_user(self):
        print(f'Good day, {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0