import unittest
from NLPToolkit.Proficiency.FryFormula import *
from .TestHelper import *


class TestFryFormula(unittest.TestCase):
    def test_happy1(self):
        value = fryFormula(text=getTestText1())
        self.assertEqual(value, 12)

    def test_happy2(self):
        value = fryFormula(text=getTestText2())
        self.assertEqual(value, 12)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            fryFormula(text=123456)


if __name__ == '__main__':
    unittest.main()
