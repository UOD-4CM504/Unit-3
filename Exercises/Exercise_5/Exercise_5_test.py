import unittest
from unittest.mock import patch
import io
import sys

class TestGradeConversion(unittest.TestCase):

    def run_program_with_inputs(self, inputs):
        inputs = iter(inputs)
        with patch('builtins.input', lambda _: next(inputs)):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(open("Exercise_5.py").read())
            sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_valid_inputs(self):
        test_cases = [
            ('0', '0 = F.'),
            ('34', '34 = F.'),
            ('35', '35 = MF.'),
            ('39', '39 = MF.'),
            ('40', '40 = D.'),
            ('49', '49 = D.'),
            ('50', '50 = C.'),
            ('59', '59 = C.'),
            ('60', '60 = B.'),
            ('69', '69 = B.'),
            ('70', '70 = A-.'),
            ('79', '79 = A-.'),
            ('80', '80 = A.'),
            ('89', '89 = A.'),
            ('90', '90 = A+.'),
            ('100', '100 = A+.')
        ]
        for input_grade, expected_output in test_cases:
            with self.subTest(input_grade=input_grade):
                output = self.run_program_with_inputs([input_grade])
                self.assertIn(expected_output, output)

    def test_invalid_inputs(self):
        test_cases = [
            ('-1', '50'),
            ('101', '75'),
            ('200', '60')  # Testing non-numeric input
        ]
        for invalid_input, valid_input in test_cases:
            with self.subTest(invalid_input=invalid_input):
                output = self.run_program_with_inputs([invalid_input, valid_input])
                self.assertIn("ERROR: input not between 0 and 100", output)
                self.assertIn(f"{valid_input} =", output)

if __name__ == '__main__':
    unittest.main()