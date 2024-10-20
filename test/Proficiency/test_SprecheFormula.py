import unittest
from LLMToolkit.Proficiency.SpracheFormula import *
from test.TestHelper import *


class TestSpracheFormula(unittest.TestCase):
    def test_happy1(self):
        value = spracheOriginalFormula(text=getTestText1())
        self.assertEqual(value, 5.39)

    def test_happy2(self):
        value = spracheOriginalFormula(text=getTestText2())
        self.assertEqual(value, 4.17)

    def test_re_happy1(self):
        value = spracheRevisedFormula(text=getTestText1())
        self.assertEqual(value, 4.71)

    def test_re_happy2(self):
        value = spracheRevisedFormula(text=getTestText2())
        self.assertEqual(value, 3.62)

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
