import sys
import io


def run_test(input_value):
    # Save the original stdin and stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    # Create string IO objects for input and output
    sys.stdin = io.StringIO(input_value + '\n')
    fake_output = io.StringIO()
    sys.stdout = fake_output

    try:
        # Execute the student's script
        with open("Exercise_1.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_positive_celsius():
    output = run_test('20.2')
    expected_prompt = "Please enter the temperature in Celsius:"
    expected_result = "20.2 Celsius is equivalent to 68.36 Fahrenheit."
    assert expected_prompt in output, f"Expected prompt '{expected_prompt}' not found in output"
    assert expected_result in output, f"Expected result '{expected_result}' not found in output"
    print("Positive Celsius test passed!")


def test_zero_celsius():
    output = run_test('0')
    expected_prompt = "Please enter the temperature in Celsius:"
    expected_result = "0.0 Celsius is equivalent to 32.0 Fahrenheit."
    assert expected_prompt in output, f"Expected prompt '{expected_prompt}' not found in output"
    assert expected_result in output, f"Expected result '{expected_result}' not found in output"
    print("Zero Celsius test passed!")


def test_negative_celsius():
    output = run_test('-1')
    expected_prompt = "Please enter the temperature in Celsius:"
    unexpected_result = "Celsius is equivalent to"
    assert expected_prompt in output, f"Expected prompt '{expected_prompt}' not found in output"
    assert unexpected_result not in output, f"Unexpected conversion result found in output: '{output}'"
    print("Negative Celsius test passed!")


def test_input_prompt():
    output = run_test('0')
    expected = "Please enter the temperature in Celsius:"
    assert expected in output, f"Expected prompt '{expected}', but got '{output}'"
    print("Input prompt test passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_positive_celsius()
    test_zero_celsius()
    test_negative_celsius()
    test_input_prompt()
    print("All tests completed!")