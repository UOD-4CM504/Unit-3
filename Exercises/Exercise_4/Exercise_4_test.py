import unittest
from unittest.mock import patch
import io
import sys

class TestSoftwarePricing(unittest.TestCase):

    def run_program_with_input(self, user_input):
        with patch('builtins.input', return_value=user_input):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(open("Exercise_4.py").read())
            sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def assertInWithEncoding(self, substring, full_string):
        # Replace the pound sign with both possible encodings
        substring = substring.replace('£', '(?:£|Â£)')
        self.assertRegex(full_string, substring)

    def test_no_discount(self):
        output = self.run_program_with_input('3')
        self.assertInWithEncoding("You have been given a 0% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £297.00.", output)

    def test_10_percent_discount(self):
        output = self.run_program_with_input('7')
        self.assertInWithEncoding("You have been given a 10% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £623.70.", output)

    def test_20_percent_discount(self):
        output = self.run_program_with_input('15')
        self.assertInWithEncoding("You have been given a 20% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £1188.00.", output)

    def test_30_percent_discount(self):
        output = self.run_program_with_input('25')
        self.assertInWithEncoding("You have been given a 30% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £1732.50.", output)

    def test_40_percent_discount(self):
        output = self.run_program_with_input('75')
        self.assertInWithEncoding("You have been given a 40% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £4455.00.", output)

    def test_50_percent_discount(self):
        output = self.run_program_with_input('150')
        self.assertInWithEncoding("You have been given a 50% discount on the normal price of £99.", output)
        self.assertInWithEncoding("The total cost is £7425.00.", output)

if __name__ == '__main__':
    unittest.main()