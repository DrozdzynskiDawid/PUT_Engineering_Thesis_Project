import unittest
from NLPToolkit.Proficiency.FleschKincaid import *
from TestHelper import *


class TestFleschKincaid(unittest.TestCase):
    def test_happy1(self):
        value = fleschKincaid(text=getTestText1())
        self.assertLess(value, 2)

    def test_happy2(self):
        value = fleschKincaid(text=getTestText2())
        self.assertLess(value, 2)

    def test_grade_happy1(self):
        value = gradeLevelFleschKincaid(text=getTestText1())
        self.assertLess(value, 2)

    def test_grade_happy2(self):
        value = gradeLevelFleschKincaid(text=getTestText2())
        self.assertLess(value, 2)

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
