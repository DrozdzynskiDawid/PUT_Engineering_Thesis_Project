import unittest
from LLMToolkit.Proficiency.LinsearWrite import *
from test.TestHelper import *


class TestLinearWhite(unittest.TestCase):
    def test_happy1(self):
        value = linsearWrite(text=getTestText1())
        self.assertGreater(value, 4)

    def test_happy2(self):
        value = linsearWrite(text=getTestText2())
        self.assertGreater(value, 6)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            linsearWrite(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            linsearWrite("")


if __name__ == '__main__':
    unittest.main()
