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
    Basic tests: names and multi-word text should be converted to initials,
    and extra whitespace should be ignored.
    """
    result = Initial().operate(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("@abc", "@A."),
        ("@G48A3", "@G."),
        ("-*-abc", "-*-A."),
    ],
)
def test_initials_with_prefix(input_text, expected):
    """
    Test that non-alphanumeric prefixes are preserved and only
    the first alphanumeric character becomes the initial.
    """
    result = Initial().operate(input_text)
    assert result == expected
