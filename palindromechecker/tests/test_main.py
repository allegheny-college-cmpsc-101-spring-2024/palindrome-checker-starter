# TODO: Add the required docstring and any required imports of objects

# TODO: Add comments to the test cases to explain how the tests works

# TODO: Review how runner.invoke works by reading the documentation
# Reference:
# https://typer.tiangolo.com/tutorial/testing/

# TODO: Write at least three additional test cases that follow the pattern of
# the provided test case. When creating oracles, you will need to think
# carefully about what output should appear in the command-line interface if
# the program contains all of the required features.

def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout


def test_palindromechecker_recursive_is_not_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    # TODO: implement this test case using the provided example


def test_palindromechecker_reverse_is_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    # TODO: implement this test case using the provided example


def test_palindromechecker_reverse_is_not_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    # TODO: implement this test case using the provided example
