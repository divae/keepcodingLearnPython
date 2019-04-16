import unittest

def is_divisible_by_four_hundred(year):
    return (year % 400) == 0 

def is_divisible_by_four(year):
    return (year % 4) == 0

def not_is_divisible_by_hundred(year):
    return (year % 100) != 0

def is_leap_year(year):
    return is_divisible_by_four_hundred(year) or (is_divisible_by_four(year) and not_is_divisible_by_hundred(year))

class TestLeapYear(unittest.TestCase):

    def test_is_divisible_by_four_hundred(self):
        year = 2000
        result = is_divisible_by_four_hundred(year)
        self.assertEqual(result,True)

    def test_is_divisible_by_four(self):
        year = 2018
        result = is_divisible_by_four_hundred(year)        
        self.assertEqual(result,False) 

    def test_not_is_divisible_by_hundred(self):
        year = 2011
        result = not_is_divisible_by_hundred(year)        
        self.assertEqual(result,True) 
    
    def test_is_leap_year(self):
        year = 2000
        result = is_leap_year(year)
        self.assertEqual(result,True)
    
    def test_not_is_leap_year(self):
        year = 2009
        result = is_leap_year(year)
        self.assertEqual(result,False)

if __name__ == "__main__":
    unittest.main()
