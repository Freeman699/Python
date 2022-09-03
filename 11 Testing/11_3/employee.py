class Employee():
    """Класс представляющий работника"""

    def __init__(self, first_name, last_name, yearly_salary):
        """Сохраняет данные о работнике"""
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = yearly_salary

    def give_raise(self, add_to_salory = 5000):
        """Увеличивает оклад"""
        self.yearly_salary += add_to_salory