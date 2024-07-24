import sys
import io


def run_program_with_inputs(inputs):
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
        with open("Exercise_5.py", "r") as file:
            exec(file.read())

        # Get the output
        output = fake_output.getvalue()
    finally:
        # Restore original stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output.strip()


def test_valid_inputs():
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
        output = run_program_with_inputs([input_grade])
        assert expected_output in output, f"For input {input_grade}, expected '{expected_output}', but got: {output}"
    print("All valid input tests passed!")


def test_invalid_inputs():
    test_cases = [
        ('-1', '50'),
        ('101', '75'),
        ('200', '60')  # Testing non-numeric input
    ]
    for invalid_input, valid_input in test_cases:
        output = run_program_with_inputs([invalid_input, valid_input])
        assert "ERROR: input not between 0 and 100" in output, f"For invalid input {invalid_input}, expected error message, but got: {output}"
        assert f"{valid_input} =" in output, f"For valid input {valid_input} after invalid input, expected grade conversion, but got: {output}"
    print("All invalid input tests passed!")


if __name__ == '__main__':
    print("Running tests...")
    test_valid_inputs()
    test_invalid_inputs()
    print("All tests completed!")