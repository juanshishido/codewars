import unittest

from kyu4.permutations import permutations


class TestPermutations(unittest.TestCase):

    def test_a_is_a(self):
        self.assertEquals(['a'], sorted(permutations('a')))

    def test_ab_is_ab_ba(self):
        self.assertEquals(['ab', 'ba'], sorted(permutations('ab')))

    def test_aabb(self):
        r = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        self.assertEquals(r, sorted(permutations('aabb')))
