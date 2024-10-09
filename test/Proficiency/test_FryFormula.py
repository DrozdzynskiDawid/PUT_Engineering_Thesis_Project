import unittest
from LLMToolkit.Proficiency.FryFormula import *
from .TestHelper import *


class TestFryFormula(unittest.TestCase):
    def test_happy1(self):
        value = fryFormula(text=getTestText1())
        self.assertGreater(value, (1.00, 0.00))

    def test_should_throw_statistic_error(self):
        with self.assertRaises(Exception):
            fryFormula(text=getTestText2())

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            fryFormula(text=123456)


if __name__ == '__main__':
    unittest.main()
