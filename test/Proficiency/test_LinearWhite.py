import unittest
from LLMToolkit.Proficiency.LinearWhite import *
from test.TestHelper import *


class TestLinearWhite(unittest.TestCase):
    def test_happy1(self):
        value = linearWhite(text=getTestText1())
        self.assertGreater(value, 5)

    def test_happy2(self):
        value = linearWhite(text=getTestText2())
        self.assertGreater(value, 6)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            linearWhite(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            linearWhite("")


if __name__ == '__main__':
    unittest.main()
