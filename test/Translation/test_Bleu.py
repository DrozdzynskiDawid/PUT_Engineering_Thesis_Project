import unittest
from LLMToolkit.Translation.Blue import Bleu
from test.TestHelper import *

class TestBleu(unittest.TestCase):
    def test_happy1(self):
        value = Bleu(reference= getTestText1, candidate= getTestText6())
        self.assertEqual(value, 0.5)

    def test_happy2(self):
        value = Bleu(reference= getTestText2, candidate= getTestText6())
        self.assertEqual(value, 0.5)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            Bleu(reference=123456, candidate=getTestText6())

    def test_should_throw_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            Bleu("", "")
        
    def test_should_throw_empty_error(self):
        with self.assertRaises(ValueError):
            Bleu("", getTestText6())
    
    def test_should_throw_empty_error(self):
        with self.assertRaises(ValueError):
            Bleu(getTestText6(), "")

if __name__ == '__main__':
    unittest.main()