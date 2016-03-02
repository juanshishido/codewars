import unittest

from kyu6.dig_pow import dig_pow


class TestDigPow(unittest.TestCase):

    def test_89_is_one(self):
        self.assertEquals(1, dig_pow(89, 1))

    def test_92_is_negone(self):
        self.assertEquals(-1, dig_pow(92, 1))

    def test_695_is_two(self):
        self.assertEquals(2, dig_pow(695, 2))

    def test_46288_is_fiftyone(self):
        self.assertEquals(51, dig_pow(46288, 3))
