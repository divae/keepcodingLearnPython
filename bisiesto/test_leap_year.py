import unittest

def is_divisible_by_four_hundred(year):
    return 1

class TestLeapYear(unittest.TestCase):

    def any_year_divisible_by_four_hundred(self):
        year = 2018

        result = is_divisible_by_four_hundred(year)

        self.assertEqual(result,True)

    def not_divisible_by_four_year_not_is_leap(self):
        year = 2018

        result = is_divisible_by_four_hundred(year)
        
        self.assertEqual(result,False)   

if __name__ == "__main__":
    unittest.main()
