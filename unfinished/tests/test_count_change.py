import unittest

from unfinished.count_change import count_change


class TestCountChange(unittest.TestCase):

    def test_count_change_4_is_3(self):
        self.assertEquals(3, count_change(4, [1, 2]))

    def test_count_change_10_is_4(self):
        self.assertEquals(4, count_change(10, [5, 2, 3]))

    def test_count_change_11_is_0(self):
        self.assertEquals(0, count_change(11, [5, 7]))

    def test_count_change_2_is_1(self):
        self.assertEquals(1, count_change(2, [2, 3]))
