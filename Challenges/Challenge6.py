import unittest
from unittest.mock import mock_open, patch
# from secret import validate_recipe, RuinedNikuldenDinnerError
from Challenge6_real import validate_recipe, RuinedNikuldenDinnerError


class TestNikuldenValidator(unittest.TestCase):
    def setUp(self):
        self.valid_contents = [
            "Рецепта за Рибена глава и СьОНГА по врачански.",
            "Рецепта за рибена чорба.",
            "Сьонга",
            "Cьонга с рибена глава за Никулден."
            "Шаран и РИБА"
        ]

        self.invalid_contents = [
            "Врачанска рецепта за вегани на Никулден.",
            "Зелена салата с домати и краставици.",
            "Печени картофи с чесън и магданоз.",
            "Супа от гъби по селски."
        ]

    def test_valid_recipe(self):
        for content in self.valid_contents:
            with patch("builtins.open", mock_open(read_data=content)):
                result = validate_recipe("random_name.txt")
                self.assertTrue(result)

    def test_invalid_recipe(self):
        for content in self.invalid_contents:
            with patch("builtins.open", mock_open(read_data=content)):
                result = validate_recipe("random_name.txt")
                self.assertFalse(result)

    def test_bad_recipe_file(self):
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("random_name.txt")

        content = "Рецепта за Рибена глава и СьОНГА по врачански."
        with patch("builtins.open", mock_open(read_data=content)) as mocket_file:
            mocket_file.return_value.read.side_effect = IOError
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("random_name.txt")

if __name__ == '__main__':
    unittest.main()
