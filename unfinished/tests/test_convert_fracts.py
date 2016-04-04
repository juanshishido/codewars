import unittest

from unfinished.convert_fracts import convert_fracts


class TestConvertFracts(unittest.TestCase):

    def test_half_third_fourth(self):
        a = [[1, 2], [1, 3], [1, 4]]
        b = [[6, 12], [4, 12], [3, 12]]
        self.assertEquals(b, convert_fracts(a))

    def test_third_fifth(self):
        a = [[1, 3], [1, 5]]
        b = [[5, 15], [3, 15]]
        self.assertEquals(b, convert_fracts(a))
