import pytest
from presidio_anonymizer.operators import Initial


def test_correct_name():
    """
    Make sure the Initial operator reports the correct name.
    """
    assert Initial().operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("John Smith", "J. S."),
        ("  Eastern   Michigan   University  ", "E. M. U."),
    ],
)
def test_initials_basic(input_text, expected):
    """
    Basic test: a simple first + last name should be converted to initials.
    """
    result = Initial().operate(input_text)
    assert result == expected
