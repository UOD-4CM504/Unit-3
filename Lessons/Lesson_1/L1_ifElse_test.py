import unittest
from unittest.mock import patch
import io
import sys

class TestEvenOddChecker(unittest.TestCase):

    def run_program_with_input(self, user_input):
        with patch('builtins.input', return_value=user_input):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(open("L1_ifElse.py").read())
            sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_even_numbers(self):
        test_cases = ['0', '2', '4', '100', '1000']
        for num in test_cases:
            with self.subTest(num=num):
                output = self.run_program_with_input(num)
                self.assertEqual(output, "Your number is even!")

    def test_odd_numbers(self):
        test_cases = ['1', '3', '5', '99', '1001']
        for num in test_cases:
            with self.subTest(num=num):
                output = self.run_program_with_input(num)
                self.assertEqual(output, "Your number is odd!")

    def test_negative_numbers(self):
        test_cases = ['-1', '-2', '-3', '-100']
        for num in test_cases:
            with self.subTest(num=num):
                output = self.run_program_with_input(num)
                self.assertEqual(output, "Your number is even!" if int(num) % 2 == 0 else "Your number is odd!")

if __name__ == '__main__':
    unittest.main()