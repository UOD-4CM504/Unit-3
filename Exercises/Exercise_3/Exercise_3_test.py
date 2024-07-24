import sys
import io


def run_test(inputs):
    # Save the original stdin and stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    # Create string IO objects for input and output
    input_string = '\n'.join(inputs) + '\n'
    sys.stdin = io.StringIO(input_string)
    fake_output = io.StringIO()
    sys.stdout = fake_output

    try:
        # Execute the student's script
        with open("Exercise_3.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_celsius_to_fahrenheit():
    output = run_test(['1', '20.2'])
    assert "20.2 Celsius is equivalent to 68.36 Fahrenheit." in output, f"Expected Celsius to Fahrenheit conversion, but got: {output}"
    print("Celsius to Fahrenheit test passed!")


def test_celsius_negative_input():
    output = run_test(['1', '-2'])
    assert "ERROR: You must enter a value of 0 or greater." in output, f"Expected error for negative Celsius input, but got: {output}"
    print("Negative Celsius input test passed!")


def test_fahrenheit_to_celsius():
    output = run_test(['2', '70.25'])
    assert "70.25 Fahrenheit is equivalent to 21.25 Celsius." in output, f"Expected Fahrenheit to Celsius conversion, but got: {output}"
    print("Fahrenheit to Celsius test passed!")


def test_fahrenheit_negative_input():
    output = run_test(['2', '-2'])
    assert "ERROR: You must enter a value of 0 or greater." in output, f"Expected error for negative Fahrenheit input, but got: {output}"
    print("Negative Fahrenheit input test passed!")


def test_invalid_option():
    output = run_test(['3'])
    assert "ERROR: Invalid option" in output, f"Expected error for invalid option, but got: {output}"
    print("Invalid option test passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_celsius_to_fahrenheit()
    test_celsius_negative_input()
    test_fahrenheit_to_celsius()
    test_fahrenheit_negative_input()
    test_invalid_option()
    print("All tests completed!")