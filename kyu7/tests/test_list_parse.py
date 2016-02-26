import unittest

from kyu7.list_parse import *


class TestListParse(unittest.TestCase):

    arr = [1, 2, 3, 4, 5]

    def test_head_one(self):
        self.assertEqual(1, head(self.arr))

    def test_tail_two_through_five(self):
        self.assertEqual([2, 3, 4, 5], tail(self.arr))

    def test_tail_one_empty(self):
        self.assertEqual([], tail([1]))

    def test_init_one_through_four(self):
        self.assertEqual([1, 2, 3, 4], init(self.arr))

    def test_last_five(self):
        self.assertEqual(5, last(self.arr))
