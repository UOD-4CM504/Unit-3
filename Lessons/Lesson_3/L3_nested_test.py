import unittest
from unittest.mock import patch
import io

class TestTemperatureConversion(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '20'])
    def test_celsius_to_fahrenheit(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            import L3_nested_if_statement  # This will run the program
            self.assertIn("20.0 Celsius is equivalent to 68.0 Fahrenheit.", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()