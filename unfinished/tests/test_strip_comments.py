import unittest

from unfinished.strip_comments import strip_comments


class TestStripComments(unittest.TestCase):

    def test_fruits_shebang(self):
        text = "apples, pears # and bananas\ngrapes\nbananas !apples"
        answer = "apples, pears\ngrapes\nbananas"
        self.assertEquals(answer, strip_comments(text, ["#", "!"]))

    def test_a_c_d(self):
        text = "a #b\nc\nd $e f g"
        answer = "a\nc\nd"
        self.assertEquals(answer, strip_comments(text, ["#", "$"]))
