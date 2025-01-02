import unittest
from LLMToolkit.Translation.Meteor import calculate_meteor
class TestCalculateMeteor(unittest.TestCase):

    def test_valid_strings(self):
        reference = "This is a sample reference"
        hypothesis = "This is a sample hypothesis"
        score = calculate_meteor(reference, hypothesis)
        self.assertTrue(score >= 0 and score <= 1)

    def test_empty_reference_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_meteor([""], "Hypothesis")


    def test_list_reference(self):
        reference = ["This", "is", "a", "sample", "reference"]
        hypothesis = "This is a sample reference"
        score = calculate_meteor(reference, hypothesis)
        self.assertTrue(score >= 0 and score <= 1)

    def test_single_word(self):
        reference = "Hello"
        hypothesis = "Hello"
        score = calculate_meteor(reference, hypothesis)
        self.assertGreaterEqual(score, 0)

if __name__ == "__main__":
    unittest.main()
