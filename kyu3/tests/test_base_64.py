import unittest

from kyu3.base_64 import *


class TestBase64(unittest.TestCase):

    def test_to_base64(self):
        answer = 'dGhpcyBpcyBhIHN0cmluZyEh'
        self.assertEquals(answer, to_base_64('this is a string!!'))

    def test_from_base64(self):
        answer = 'this is a string!!'
        self.assertEquals(answer, from_base_64('dGhpcyBpcyBhIHN0cmluZyEh'))

    def test_codewars_tests(self):
        tests = [
                 ["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
                 ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
                 ["now is the time for all good men to come to the aid of their country.",
                  "bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
                 ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
                 ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
                 ["the quick brown fox jumps over the white fence. ",
                  "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
                 ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4",
                  "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
                 ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
                 ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]
                ]
        for test in tests:
            result = to_base_64(test[0])
            self.assertEquals(result, test[1])
            self.assertEquals(from_base_64(result), test[0])
