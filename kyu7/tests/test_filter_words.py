import unittest

from kyu7.filter_words import filter_words


class TestFilterWords(unittest.TestCase):

    def test_Bad(self):
        self.assertEqual("You're awesome! timmy!",
                         filter_words("You're Bad! timmy!"))

    def test_MEAN(self):
        self.assertEqual("You're awesome! timmy!",
                         filter_words("You're MEAN! timmy!"))
