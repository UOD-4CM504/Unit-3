import sys
import io
import re


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
        with open("Exercise_4.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def assert_in_with_encoding(substring, full_string):
    # Replace the pound sign with both possible encodings
    substring = substring.replace('£', '(?:£|Â£)')
    assert re.search(substring, full_string), f"Expected '{substring}' in output, but got: {full_string}"


def test_no_discount():
    output = run_program_with_input('3')
    assert_in_with_encoding("You have been given a 0% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £297.00.", output)
    print("No discount test passed!")


def test_10_percent_discount():
    output = run_program_with_input('7')
    assert_in_with_encoding("You have been given a 10% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £623.70.", output)
    print("10% discount test passed!")


def test_20_percent_discount():
    output = run_program_with_input('15')
    assert_in_with_encoding("You have been given a 20% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £1188.00.", output)
    print("20% discount test passed!")


def test_30_percent_discount():
    output = run_program_with_input('25')
    assert_in_with_encoding("You have been given a 30% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £1732.50.", output)
    print("30% discount test passed!")


def test_40_percent_discount():
    output = run_program_with_input('75')
    assert_in_with_encoding("You have been given a 40% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £4455.00.", output)
    print("40% discount test passed!")


def test_50_percent_discount():
    output = run_program_with_input('150')
    assert_in_with_encoding("You have been given a 50% discount on the normal price of £99.", output)
    assert_in_with_encoding("The total cost is £7425.00.", output)
    print("50% discount test passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_no_discount()
    test_10_percent_discount()
    test_20_percent_discount()
    test_30_percent_discount()
    test_40_percent_discount()
    test_50_percent_discount()
    print("All tests completed!")