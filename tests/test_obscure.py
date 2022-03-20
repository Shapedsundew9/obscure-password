"""Units tests for obscure_password."""
from random import choices, randint
from string import printable

import pytest
from obscure_password import obscure, unobscure


@pytest.mark.parametrize("_", range(1000))
def test_random_obscurity(_):
    """Check obfuscation for 1000 randomly generated ASCII strings."""
    text = ''.join(choices(printable, k=randint(1, 1024)))
    assert unobscure(obscure(text)) == text


@pytest.mark.parametrize("phrase",
                         (
                             '你好',
                             'Nǐ hǎo',
                             '早上好',
                             'Zǎoshang hǎo',
                             '混淆很有趣',
                             'Hùnxiáo hěn yǒuqù',
                             '感谢 LifelongStew7 发现了非 ASCII 字符错误！',
                             'Gǎnxiè LifelongStew7 fāxiànle fēi ASCII zìfú cuòwù!'
                         )
                         )
def test_non_ascii(phrase):
    """Some Chinese phrases."""
    assert unobscure(obscure(phrase)) == phrase


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
