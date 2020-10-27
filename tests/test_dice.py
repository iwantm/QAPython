import pytest

from programs import dice


def test_dice():
    num = dice.dice()
    assert 1 <= num <= 6
