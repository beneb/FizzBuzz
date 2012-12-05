import random
import unittest

class FizzBuzz():
    def fizz_buzz(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return 'fizzbuzz'

        if number % 3 == 0:
            return 'fizz'

        if number % 5 == 0:
            return 'buzz'
        
        return str(number)

class FizzBuzzTests(unittest.TestCase):

    def setUp(self):
        self.fb = FizzBuzz()
        
    def test_one_gets_one(self):
        self.assertEqual('1', self.fb.fizz_buzz(1))
 
    def test_three_gets_fizz(self):
        self.assertEqual('fizz', self.fb.fizz_buzz(3))
 
    def test_five_gets_buzz(self):
        self.assertEqual('buzz', self.fb.fizz_buzz(5))

    def test_six_gets_fizz(self):
        self.assertEqual('fizz', self.fb.fizz_buzz(6))

    def test_fifteen_gets_fizzbuzz(self):
        self.assertEqual('fizzbuzz', self.fb.fizz_buzz(15))


if __name__ == '__main__':
    unittest.main()

