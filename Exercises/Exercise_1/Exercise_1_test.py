import unittest
from unittest.mock import patch
import io
import sys


class TestCelsiusToFahrenheitConverter(unittest.TestCase):

    @patch('builtins.input', return_value='20.2')
    def test_positive_celsius(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_1.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("20.2 Celsius is equivalent to 68.36 Fahrenheit.", captured_output.getvalue())

    @patch('builtins.input', return_value='0')
    def test_zero_celsius(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_1.py").read())

        sys.stdout = sys.__stdout__
        self.assertIn("0.0 Celsius is equivalent to 32.0 Fahrenheit.", captured_output.getvalue())

    @patch('builtins.input', return_value='-1')
    def test_negative_celsius(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(open("Exercise_1.py").read())

        sys.stdout = sys.__stdout__
        self.assertEqual("", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()