import unittest

from kyu6.multiplication_table import multiplication_table


class TestMultiplicationTable(unittest.TestCase):

    def test_two_by_two(self):
        self.assertEquals([[1,2],[2,4]], multiplication_table(2,2))

    def test_three_by_three(self):
        self.assertEquals([[1,2,3],[2,4,6],[3,6,9]], multiplication_table(3,3))

    def test_three_by_four(self):
        self.assertEquals([[1, 2, 3, 4],[2, 4, 6, 8],[3, 6, 9, 12]],
                          multiplication_table(3, 4))
