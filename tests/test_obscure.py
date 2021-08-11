"""Units tests for obscure_password."""
from random import choices, randint
from string import printable

from obscure_password import obscure, unobscure


def test_random_obscurity():
    """Check obfuscation for 1000 randomly generated ASCII strings."""
    for _ in range(1000):
        text = ''.join(choices(printable, k=randint(1, 1024)))
        assert unobscure(obscure(text)) == text


def test_random_unmarked():
    """Check unobscure does not modify 1000 randomly generated ASCII strings."""
    for _ in range(1000):
        text = ''.join(choices(printable, k=randint(1, 1024)))
        assert unobscure(text) == text


def test_corner_0():
    """Check lifecycle works with a single character string."""
    text = 'i'
    assert unobscure(obscure(text)) == text
    assert unobscure(text) == text


def test_corner_1():
    """Check lifecycle works with a zero length string."""
    text = ''
    assert unobscure(obscure(text)) == text
    assert unobscure(text) == text
