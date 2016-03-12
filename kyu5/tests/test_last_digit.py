import unittest

from kyu5.last_digit import last_digit


class TestLastDigit(unittest.TestCase):

    def test_three_to_the_eight_is_one(self):
        self.assertEquals(1, last_digit(3, 8))

    def test_four_to_the_first_is_four(self):
        self.assertEquals(4, last_digit(4, 1))

    def test_four_to_the_second_is_six(self):
        self.assertEquals(6, last_digit(4, 2))

    def test_nine_to_the_seventh_is_nine(self):
        self.assertEquals(9, last_digit(9, 7))

    def test_ten_to_the_ten_to_the_ten_is_zero(self):
        self.assertEquals(0, last_digit(10, 10 ** 10))

    def test_two_to_the_200_to_the_two_to_the_300_is_six(self):
        self.assertEquals(6, last_digit(2 ** 200, 2 ** 300))
