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
        with open("L3_nested_if_statement.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_divisible_by_3_and_5():
    output = run_program_with_input('15')
    expected = "Your number is divisible by 3 and 5."
    assert expected in output, f"Expected '{expected}' in output, but got: {output}"
    print("Test for number divisible by 3 and 5 passed!")


def test_divisible_by_3_not_5():
    output = run_program_with_input('9')
    expected = "Your number is divisible by 3 and NOT by 5."
    assert expected in output, f"Expected '{expected}' in output, but got: {output}"
    print("Test for number divisible by 3 but not 5 passed!")


def test_divisible_by_5_not_3():
    output = run_program_with_input('10')
    expected = "Your number is NOT divisible by 3 and is divisible by 5."
    assert expected in output, f"Expected '{expected}' in output, but got: {output}"
    print("Test for number divisible by 5 but not 3 passed!")


def test_not_divisible_by_3_or_5():
    output = run_program_with_input('7')
    expected = "Your number is NOT divisible by 3 and 5."
    assert expected in output, f"Expected '{expected}' in output, but got: {output}"
    print("Test for number not divisible by 3 or 5 passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_divisible_by_3_and_5()
    test_divisible_by_3_not_5()
    test_divisible_by_5_not_3()
    test_not_divisible_by_3_or_5()
    print("All tests completed!")