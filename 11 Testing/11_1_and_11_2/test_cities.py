import unittest
import city_functions

class CityFuncTestCase(unittest.TestCase):
    '''Тесты для "city_functions.py"'''

    def test_city_country(self):
        """Does func works with this kind of data: ''Kiev', 'Ukraine'' ?"""
        formated_city = city_functions.get_formatted_city_name('Kiev', 'Ukraine')
        self.assertEqual(formated_city, 'Kiev, Ukraine')

    def test_city_country_population(self):
        """Does func works with this kind of data: ''Berlin', 'Germany', '1000000'' ?"""
        formated_city = city_functions.get_formatted_city_name('Berlin', 'Germany', '1000000')

if __name__ == '__main__':
    unittest.main()