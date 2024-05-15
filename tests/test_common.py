"""Test module for common functions."""

from libtemp.common import concatenate_strings

def test_string_concatenation() -> None:
    """Unit test for the string concatenation function. """
    concatenated = concatenate_strings(["hello", " ", "world"])
    assert concatenated == "hello world"
