import pytest
from rhllasag_package.__main__ import CustomClass


def test_get_info():
    dev = CustomClass("Python")
    assert dev.get_info() == "Alice is a developer who codes in Python."


def test_invalid_language():
    with pytest.raises(ValueError):
        dev = CustomClass("English")
