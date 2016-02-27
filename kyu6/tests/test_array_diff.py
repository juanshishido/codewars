import unittest

from kyu6.array_diff import array_diff


class TestArrayDiff(unittest.TestCase):

    def test_onetwo_one(self):
        self.assertEquals([2], array_diff([1, 2], [1]))

    def test_onetwotwo_one(self):
        self.assertEquals([2, 2], array_diff([1,2,2], [1]))

    def test_onetwotwo_two(self):
        self.assertEquals([1], array_diff([1, 2, 2], [2]))

    def test_onetwotwo_empty(self):
        self.assertEquals([1, 2, 2], array_diff([1, 2, 2], []))

    def test_empty_onetwo(self):
        self.assertEquals([], array_diff([], [1, 2]))
