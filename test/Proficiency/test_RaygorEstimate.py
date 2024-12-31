import unittest
from LLMToolkit.Proficiency.RaygorEstimate import *
from test.TestHelper import *


class TestRayor(unittest.TestCase):
    def test_happy1(self):
        value = raygorEstimate(text=getTestText1())
        self.assertEqual(value, (36.54, 4.81))

    def test_happy2(self):
        value = raygorEstimate(text=getTestText1()+getTestText2()+getTestText2())
        self.assertEqual(value, (30.62, 5.74))

    def test_happy3(self):
        value = raygorEstimate(text=getTestText3())
        self.assertEqual(value, (34.25, 4.11))

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            raygorEstimate(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(Exception):
            raygorEstimate(text="")


if __name__ == '__main__':
    unittest.main()
