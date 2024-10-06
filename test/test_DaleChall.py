import unittest
from NLPToolkit.Proficiency.DaleChall import *
from TestHelper import *


class TestDaleChall(unittest.TestCase):
    def test_happy1(self):
        value = daleChall(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = daleChall(text=getTestText2())
        self.assertLess(value, 2)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            daleChall(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            daleChall("")


if __name__ == '__main__':
    unittest.main()
