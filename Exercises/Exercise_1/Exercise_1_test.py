import unittest
from unittest.mock import patch
import io
import sys
import re


class TestCelsiusToFahrenheitConverter(unittest.TestCase):

    def run_program_and_capture_output(self, input_value):
        with patch('builtins.input', return_value=input_value):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(open("Exercise_1.py").read())
            sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_positive_celsius(self):
        output = self.run_program_and_capture_output('20.2')
        self.assertRegex(output, r"20\.2\s*Celsius is equivalent to 68\.36\s*Fahrenheit")

    def test_zero_celsius(self):
        output = self.run_program_and_capture_output('0')
        self.assertRegex(output, r"0\.0?\s*Celsius is equivalent to 32\.0?\s*Fahrenheit")

    def test_negative_celsius(self):
        output = self.run_program_and_capture_output('-1')
        self.assertRegex(output, r"ERROR:\s*You must enter a value of 0 or greater")

    def test_input_prompt(self):
        with patch('builtins.input', return_value='0') as mock_input:
            self.run_program_and_capture_output('0')
            # Check if the prompt is either in the input or printed separately
            call_args = mock_input.call_args[0][0] if mock_input.call_args else ""
            self.assertTrue(
                "Please enter the temperature in Celsius:" in call_args or
                re.search(r"Please enter the temperature in Celsius:", self.run_program_and_capture_output('0'))
            )


if __name__ == '__main__':
    unittest.main()
