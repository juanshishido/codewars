import unittest

from kyu7.search_names import search_names


class TestSearchNames(unittest.TestCase):

    def test_foo_bar(self):
        self.assertEqual([['bar_', 'bar@bar.com']],
                         search_names([['foo', 'foo@foo.com'],
                                       ['bar_', 'bar@bar.com']]))
