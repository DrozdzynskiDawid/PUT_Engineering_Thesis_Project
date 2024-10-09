import unittest
from LLMToolkit.Proficiency.GunningFog import *
from .TestHelper import *


class TestGunningFog(unittest.TestCase):
    def test_happy1(self):
        value = gunningFog(text=getTestText1())
        self.assertEqual(value, 10.89)

    def test_happy2(self):
        value = gunningFog(text=getTestText2())
        self.assertEqual(value, 7.23)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            gunningFog(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            gunningFog("")


if __name__ == '__main__':
    unittest.main()
