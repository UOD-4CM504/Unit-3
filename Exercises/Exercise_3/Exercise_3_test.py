import unittest
from unittest.mock import patch
import io
import sys


class TestTemperatureConverter(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '20.2'])
    def test_celsius_to_fahrenheit(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # We need to use execfile() to run the script in the current namespace
        exec(open("Exercise_3.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("20.2 Celsius is equivalent to 68.36 Fahrenheit.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['1', '-2'])
    def test_celsius_negative_input(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_3.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("ERROR: You must enter a value of 0 or greater.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['2', '70.25'])
    def test_fahrenheit_to_celsius(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_3.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("70.25 Fahrenheit is equivalent to 21.25 Celsius.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['2', '-2'])
    def test_fahrenheit_negative_input(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_3.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("ERROR: You must enter a value of 0 or greater.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['3'])
    def test_invalid_option(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_3.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("ERROR: Invalid option", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()