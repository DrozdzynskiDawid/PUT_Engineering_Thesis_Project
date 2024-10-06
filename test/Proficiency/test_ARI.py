import unittest
from NLPToolkit.Proficiency.AutomatedReadabilityIndex import ARI
from .TestHelper import *


class TestARI(unittest.TestCase):
    def test_happy1(self):
        value = ARI(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = ARI(text=getTestText2())
        self.assertLess(value, 2)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            ARI(text=123456)

    def test_should_throw_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            ARI("")


if __name__ == '__main__':
    unittest.main()
