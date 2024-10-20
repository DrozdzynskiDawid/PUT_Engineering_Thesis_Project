import unittest
from LLMToolkit.Proficiency.SMOG import *
from test.TestHelper import *


class TestSMOG(unittest.TestCase):
    def test_happy(self):
        value = readabilitySMOG(text=getTestText3()+getTestText1())
        self.assertEqual(value, 10.41)

    def test_easy_happy(self):
        value = easierSMOG(text=getTestText3()+getTestText1())
        self.assertEqual(value, 10)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            readabilitySMOG(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(Exception):
            readabilitySMOG(text=getTestText1())

    def test_easy_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            easierSMOG(text=123456)

    def test_easy_should_throw_error(self):
        with self.assertRaises(Exception):
            easierSMOG(text=getTestText1())


if __name__ == '__main__':
    unittest.main()
