import unittest
from LLMToolkit.Proficiency.RaygorEstimate import *
from .TestHelper import *


class TestRayor(unittest.TestCase):
    def test_happy1(self):
        value = raygorEstimate(text=getTestText1())
        self.assertEqual(value, (5.24, 0.97))

    def test_happy2(self):
        value = raygorEstimate(text=getTestText1()+getTestText2()+getTestText2())
        self.assertEqual(value, (4.77, 0.81))

    def test_happy3(self):
        value = raygorEstimate(text=getTestText3())
        self.assertEqual(value, (4.73, 0.75))

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            raygorEstimate(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(Exception):
            raygorEstimate(text="")


if __name__ == '__main__':
    unittest.main()
