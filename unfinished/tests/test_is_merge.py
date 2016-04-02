import unittest

from unfinished.is_merge import is_merge


class TestIsMerge(unittest.TestCase):

    codewars = 'codewars'

    def test_code_wars(self):
        self.assertEquals(True, is_merge(self.codewars, 'code', 'wars'))

    def test_cdoe_wars(self):
        self.assertEquals(False, is_merge(self.codewars, 'cdoe', 'wars'))

    def test_cdw_oears(self):
        self.assertEquals(True, is_merge(self.codewars, 'cdw', 'oears'))

    def test_cod_wars(self):
        self.assertEquals(False, is_merge(self.codewars, 'cod', 'wars'))
