import unittest

from kyu5.pig_it import pig_it


class TestPigIt(unittest.TestCase):

    def test_Pig_latin_is_cool(self):
        self.assertEquals('igPay atinlay siay oolcay',
                          pig_it('Pig latin is cool'))

    def test_This_is_my_string(self):
        self.assertEquals('hisTay siay ymay tringsay',
                          pig_it('This is my string'))

    def test_uisQay_ustodietcay_psosiay_ustodescay(self):
        pigged = 'uisQay ustodietcay psosiay ustodescay ?'
        to_pig = 'Quis custodiet ipsos custodes ?'
        self.assertEquals(pigged, pig_it(to_pig))
