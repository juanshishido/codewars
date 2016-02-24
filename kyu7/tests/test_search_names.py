import unittest

from kyu7.search_names import search_names


class TestAccum(unittest.TestCase):

    def test_foo_bar(self):
        self.assertEqual([['bar_', 'bar@bar.com']],
                         search_names([['foo', 'foo@foo.com'],
                                       ['bar_', 'bar@bar.com']]))
