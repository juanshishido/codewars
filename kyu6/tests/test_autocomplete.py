import unittest

from kyu6.autocomplete import autocomplete


class TestAutocomplete(unittest.TestCase):

    dictionary = ['abnormal', 'arm-wrestling', 'absolute', 'airplane',
                  'airport', 'amazing', 'apple', 'ball' ]

    def test_ai(self):
        self.assertEquals(['airplane', 'airport'],
                          autocomplete('ai', self.dictionary))

    def test_a(self):
        self.assertEquals(['abnormal', 'arm-wrestling',
                           'absolute', 'airplane', 'airport'],
                          autocomplete('a', self.dictionary))

    def test_nonalpha(self):
        self.assertEquals(['ball'], autocomplete('b$%^', self.dictionary))
