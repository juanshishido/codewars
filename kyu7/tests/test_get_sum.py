import unittest

from kyu7.get_sum import get_sum


class TestAccum(unittest.TestCase):

    def test_one_zero_equals_one(self):
        self.assertEqual(1, get_sum(1, 0))

    def test_one_two_equals_three(self):
        self.assertEqual(3, get_sum(1, 2))

    def test_zero_one_equals_one(self):
        self.assertEqual(1, get_sum(0, 1))

    def test_one_one_equals_one(self):
        self.assertEqual(1, get_sum(1, 1))

    def test_negone_zero_equals_negone(self):
        self.assertEqual(-1, get_sum(-1, 0))

    def test_negone_two_equals_two(self):
        self.assertEqual(2, get_sum(-1, 2))
