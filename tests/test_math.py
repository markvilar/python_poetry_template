"""Test module for math functions."""

from libtemp.math import add, multiply

def test_add() -> None:
    """Unit test for the add function."""
    result = add(1.0, 2.0)
    assert isinstance(result, float)
    assert result == 3.0

def test_multiply() -> None:
    """Unit test for the multiple function."""
    result = multiply(1.0, 2.0)
    assert isinstance(result, float)
    assert result == 2.0
