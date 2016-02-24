import unittest

from kyu7.xo import xo


class TestAccum(unittest.TestCase):

    def test_ooxx_True(self):
        self.assertEqual(True, xo('ooxx'))

    def test_xooxx_False(self):
        self.assertEqual(False, xo('xooxx'))

    def test_ooxXm_True(self):
        self.assertEqual(True, xo('ooxXm'))

    def test_zpzpzpp_True(self):
        self.assertEqual(True, xo('zpzpzpp'))

    def test_zzoo_False(self):
        self.assertEqual(False, xo('zzoo'))
