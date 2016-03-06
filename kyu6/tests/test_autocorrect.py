import unittest

from kyu6.autocorrect import autocorrect


class TestAutocorrect(unittest.TestCase):

    def test_u(self):
        self.assertEquals('your sister', autocorrect('u'))

    def test_you(self):
        self.assertEquals('your sister', autocorrect('you'))

    def test_You(self):
        self.assertEquals('your sister', autocorrect('You'))

    def test_Youuuuu(self):
        self.assertEquals('your sister', autocorrect('Youuuuu'))

    def test_youtube(self):
        self.assertEquals('youtube', autocorrect('youtube'))

    def test_bayou(self):
        self.assertEquals('bayou', autocorrect('bayou'))

    def test_I_miss(self):
        self.assertEquals('I miss your sister!', autocorrect('I miss u!'))
