import unittest
from LLMToolkit.Proficiency.FleschKincaid import *
from test.TestHelper import *


class TestFleschKincaid(unittest.TestCase):
    def test_happy1(self):
        value = fleschKincaid(text=getTestText1())
        self.assertEqual(value, 60.19)

    def test_happy2(self):
        value = fleschKincaid(text=getTestText2())
        self.assertEqual(value, 84.84)

    def test_grade_happy1(self):
        value = gradeLevelFleschKincaid(text=getTestText1())
        self.assertEqual(value, 10.12)

    def test_grade_happy2(self):
        value = gradeLevelFleschKincaid(text=getTestText2())
        self.assertEqual(value, 5.4)

    def test_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            fleschKincaid(text=123456)

    def test_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            fleschKincaid("")

    def test_grade_should_throw_type_error(self):
        with self.assertRaises(ValueError):
            gradeLevelFleschKincaid(text=123456)

    def test_grade_should_throw_error(self):
        with self.assertRaises(ZeroDivisionError):
            gradeLevelFleschKincaid("")



if __name__ == '__main__':
    unittest.main()
