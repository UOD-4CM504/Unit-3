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
        with open("L1_ifElse.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_even_numbers():
    test_cases = ['0', '2', '4', '100', '1000']
    for num in test_cases:
        output = run_program_with_input(num)
        assert "Your number is even!" in output, f"For input {num}, expected 'Your number is even!', but got: {output}"
    print("All even number tests passed!")


def test_odd_numbers():
    test_cases = ['1', '3', '5', '99', '1001']
    for num in test_cases:
        output = run_program_with_input(num)
        assert "Your number is odd!" in output, f"For input {num}, expected 'Your number is odd!', but got: {output}"
    print("All odd number tests passed!")


def test_negative_numbers():
    test_cases = ['-1', '-2', '-3', '-100']
    for num in test_cases:
        output = run_program_with_input(num)
        expected = "Your number is even!" if int(num) % 2 == 0 else "Your number is odd!"
        assert expected in output, f"For input {num}, expected '{expected}', but got: {output}"
    print("All negative number tests passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_even_numbers()
    test_odd_numbers()
    test_negative_numbers()
    print("All tests completed!")