import unittest

from fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
    def setUp(self):
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


    def test_has_number_been_inputted(self):
        self.assertEqual(1, fizz_buzz(self.numbers[1]))

    def test_is_number_divisible_by_3(self):
        self.assertEqual("Fizz", fizz_buzz(self.numbers[3]))

    def test_is_number_not_divisible_by_3(self):
        self.assertEqual(4, fizz_buzz(self.numbers[4]))