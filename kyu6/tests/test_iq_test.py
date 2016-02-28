import unittest

from kyu6.iq_test import iq


class TestIqTest(unittest.TestCase):

    def test_two_four_seven_eight_ten(self):
        self.assertEquals(3, iq('2 4 7 8 10'))

    def test_one_two_two(self):
        self.assertEquals(1, iq('1 2 2'))
