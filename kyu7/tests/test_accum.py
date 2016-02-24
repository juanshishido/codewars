import unittest

from kyu7.accum import accum


class TestAccum(unittest.TestCase):

    def test_abcd(self):
        self.assertEqual('A-Bb-Ccc-Dddd', accum('abcd'))

    def test_RqaEzty(self):
        self.assertEqual('R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy', accum('RqaEzty'))

    def test_cwAt(self):
        self.assertEqual('C-Ww-Aaa-Tttt', accum('cwAt'))
