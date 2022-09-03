from email.policy import default
import unittest
from  employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание стандартного работника и зарплаты для него"""
        self.salary = 1500
        self.class_employee = Employee('Maxon', 'Strangler', self.salary)

    def test_give_default_raise(self):
        """Проверка стандартной прибавки к зарплате"""
        salary = 3000
        default_raise = 5000
        my_employee = Employee('Bob', 'Hogan', salary)
        my_employee.give_raise()
        self.assertEqual(my_employee.yearly_salary, salary + default_raise)

    def test_give_custom_raise(self):
        """Проверка заданной прибавки к зарплате"""
        salary = 1500
        new_raise = 2500
        my_employee = Employee('Maxon', 'Strangler', salary)
        my_employee.give_raise(new_raise)
        self.assertEqual(my_employee.yearly_salary, salary + new_raise)

    def test_setUp_give_default_raise(self):
        """Проверка стандартной прибавки к зарплате (с использованием setUp)"""
        default_raise = 5000
        self.class_employee.give_raise()
        self.assertEqual(
            self.class_employee.yearly_salary,
            self.salary + default_raise
            )

    def test_setUp_give_custom_raise(self):
        """Проверка заданной прибавки к зарплате (с использованием setUp)"""
        new_raise = 2500
        self.class_employee.give_raise(new_raise)
        self.assertEqual(
            self.class_employee.yearly_salary,
            self.salary + new_raise
            )

if __name__ == '__main__':
    unittest.main()