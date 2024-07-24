import sys
import io


def run_program(user_input):
    # Save the original stdin and stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    # Create string IO objects for input and output
    sys.stdin = io.StringIO(user_input + '\n')
    fake_output = io.StringIO()
    sys.stdout = fake_output

    try:
        # Execute the student's script
        with open("Exercise_2.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_positive_temperature():
    output = run_program("20.2")
    assert "20.2 Celsius is equivalent to" in output, f"Expected '20.2 Celsius is equivalent to' in output, but got: {output}"
    assert "68.36 Fahrenheit" in output, f"Expected '68.36 Fahrenheit' in output, but got: {output}"
    print("Positive temperature test passed!")


def test_zero_temperature():
    output = run_program("0")
    assert "0 Celsius is equivalent to" in output, f"Expected '0 Celsius is equivalent to' in output, but got: {output}"
    assert "32.0 Fahrenheit" in output, f"Expected '32.0 Fahrenheit' in output, but got: {output}"
    print("Zero temperature test passed!")


def test_negative_temperature():
    output = run_program("-2")
    assert "ERROR: You must enter a value of 0 or greater" in output, f"Expected error message for negative input, but got: {output}"
    print("Negative temperature test passed!")


def test_input_prompt():
    output = run_program("20")
    assert "Please enter the temperature in Celsius" in output, f"Expected input prompt in output, but got: {output}"
    print("Input prompt test passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_positive_temperature()
    test_zero_temperature()
    test_negative_temperature()
    test_input_prompt()
    print("All tests completed!")