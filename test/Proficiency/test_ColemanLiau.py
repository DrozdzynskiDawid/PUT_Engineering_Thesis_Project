import unittest
from NLPToolkit.Proficiency.ColemanLiau import *
from .TestHelper import *


class TestColemanLiau(unittest.TestCase):
    def test_happy1(self):
        value = colemanLiau(text=getTestText1())
        self.assertEqual(value, 12.14)

    def test_happy2(self):
        value = colemanLiau(text=getTestText2())
        self.assertEqual(value, 6.75)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            colemanLiau(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            colemanLiau("")


if __name__ == '__main__':
    unittest.main()
