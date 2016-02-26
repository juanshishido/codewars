import unittest

from kyu7.amicable_numbers import amicable_numbers


class TestAmicableNumbers(unittest.TestCase):

    def test_220_284(self):
        self.assertEquals(True, amicable_numbers(220, 284))

    def test_220_280(self):
        self.assertEquals(False, amicable_numbers(220, 280))

    def test_1184_1210(self):
        self.assertEquals(True, amicable_numbers(1184, 1210))

    def test_220221_282224(self):
        self.assertEquals(False, amicable_numbers(220221, 282224))

    def test_10744_10856(self):
        self.assertEquals(True, amicable_numbers(10744, 10856))

    def test_299920_9284(self):
        self.assertEquals(False, amicable_numbers(299920, 9284))

    def test_999220_2849(self):
        self.assertEquals(False, amicable_numbers(999220, 2849))

    def test_122265_139815(self):
        self.assertEquals(True, amicable_numbers(122265, 139815))
