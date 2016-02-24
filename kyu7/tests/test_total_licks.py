import unittest

from kyu7.total_licks import total_licks


class TestAccum(unittest.TestCase):

    def test_freezing_temps_260(self):
        self.assertEqual('It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps.',
                         total_licks({"freezing temps": 10, "clear skies": -2}))

    def test_not_empty_245(self):
        self.assertEqual('It took 245 licks to get to the tootsie roll center of a tootsie pop.',
                         total_licks({"happiness": -5, "clear skies": -2}))

    def test_empty_252(self):
        self.assertEqual('It took 252 licks to get to the tootsie roll center of a tootsie pop.',
                         total_licks({}))

    def test_evil_wizards_512(self):
        self.assertEqual('It took 512 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was evil wizards.',
                         total_licks({"dragons": 100,
                                      "evil wizards": 110,
                                      "trolls": 50}))

    def test_not_empty_2(self):
        self.assertEqual('It took 2 licks to get to the tootsie roll center of a tootsie pop.',
                         total_licks({"white magic": -250}))
