import unittest
from unittest.mock import patch
import io
import sys

class TestNumberClassification(unittest.TestCase):

    def run_program_with_input(self, user_input):
        with patch('builtins.input', return_value=user_input) as mock_input:
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(open("L2_elif_statement.py").read())
            sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip(), mock_input

    def test_positive_numbers(self):
        test_cases = ['2.3', '1', '0.1', '100.5']
        for num in test_cases:
            with self.subTest(num=num):
                output, _ = self.run_program_with_input(num)
                self.assertEqual(output, "Your number is positive!")

    def test_negative_numbers(self):
        test_cases = ['-3.3', '-1', '-0.1', '-100.5']
        for num in test_cases:
            with self.subTest(num=num):
                output, _ = self.run_program_with_input(num)
                self.assertEqual(output, "Your number is negative!")

    def test_zero(self):
        output, _ = self.run_program_with_input('0')
        self.assertEqual(output, "Your number is zero!")

    def test_input_prompt(self):
        _, mock_input = self.run_program_with_input('1')
        mock_input.assert_called_with("Please enter a number:\n")

    def test_float_input(self):
        test_cases = ['2.3', '-3.3', '0.0']
        for num in test_cases:
            with self.subTest(num=num):
                output, _ = self.run_program_with_input(num)
                self.assertIn("Your number is", output)

if __name__ == '__main__':
    unittest.main()