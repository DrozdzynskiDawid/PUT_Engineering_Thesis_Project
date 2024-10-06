import unittest
from NLPToolkit.Proficiency.FORCAST import *
from .TestHelper import *


class TestFORCAST(unittest.TestCase):
    def test_happy1(self):
        value = forcast(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = forcast(text=getTestText2())
        self.assertLess(value, 2)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            forcast(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            forcast("")


if __name__ == '__main__':
    unittest.main()
