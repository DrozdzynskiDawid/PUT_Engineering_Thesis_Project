import unittest
from NLPToolkit.Proficiency.ColemanLiau import *
from .TestHelper import *


class TestColemanLiau(unittest.TestCase):
    def test_happy1(self):
        value = colemanLiau(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = colemanLiau(text=getTestText2())
        self.assertLess(value, 2)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            colemanLiau(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            colemanLiau("")


if __name__ == '__main__':
    unittest.main()
