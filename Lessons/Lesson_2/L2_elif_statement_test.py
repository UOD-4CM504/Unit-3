import sys
import io


def run_program_with_input(user_input):
    # Save the original stdin and stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    # Create string IO objects for input and output
    sys.stdin = io.StringIO(user_input + '\n')
    fake_output = io.StringIO()
    sys.stdout = fake_output

    try:
        # Execute the student's script
        with open("L2_elif_statement.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_positive_numbers():
    test_cases = ['2.3', '1', '0.1', '100.5']
    for num in test_cases:
        output = run_program_with_input(num)
        assert "Your number is positive!" in output, f"For input {num}, expected 'Your number is positive!', but got: {output}"
    print("All positive number tests passed!")


def test_negative_numbers():
    test_cases = ['-3.3', '-1', '-0.1', '-100.5']
    for num in test_cases:
        output = run_program_with_input(num)
        assert "Your number is negative!" in output, f"For input {num}, expected 'Your number is negative!', but got: {output}"
    print("All negative number tests passed!")


def test_zero():
    output = run_program_with_input('0')
    assert "Your number is zero!" in output, f"For input 0, expected 'Your number is zero!', but got: {output}"
    print("Zero test passed!")


def test_input_prompt():
    output = run_program_with_input('1')
    assert "Please enter a number:" in output, f"Expected input prompt 'Please enter a number:', but it was not found in the output: {output}"
    print("Input prompt test passed!")


def test_float_input():
    test_cases = ['2.3', '-3.3', '0.0']
    for num in test_cases:
        output = run_program_with_input(num)
        assert "Your number is" in output, f"For float input {num}, expected 'Your number is' in output, but got: {output}"
    print("All float input tests passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_positive_numbers()
    test_negative_numbers()
    test_zero()
    test_input_prompt()
    test_float_input()
    print("All tests completed!")