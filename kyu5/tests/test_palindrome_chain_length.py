import unittest

from kyu5.palindrome_chain_length import palindrome_chain_length


class TestPCL(unittest.TestCase):

    def test_87_is_4(self):
        self.assertEquals(4, palindrome_chain_length(87))

    def test_171_is_0(self):
        self.assertEquals(0, palindrome_chain_length(171))
