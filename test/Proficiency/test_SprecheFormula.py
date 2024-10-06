import unittest
from NLPToolkit.Proficiency.SpracheFormula import *
from .TestHelper import *


class TestSpracheFormula(unittest.TestCase):
    def test_happy1(self):
        value = spracheOriginalFormula(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = spracheOriginalFormula(text=getTestText2())
        self.assertLess(value, 2)

    def test_re_happy1(self):
        value = spracheRevisedFormula(text=getTestText1())
        self.assertLess(value, 2)

    def test_re_happy2(self):
        value = spracheRevisedFormula(text=getTestText2())
        self.assertLess(value, 2)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            spracheOriginalFormula(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            spracheOriginalFormula("")

    def test_re_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            spracheRevisedFormula(text=123456)

    def test_re_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            spracheRevisedFormula("")


if __name__ == '__main__':
    unittest.main()
