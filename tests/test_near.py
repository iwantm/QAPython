import pytest
from programs import near


def test_near_reset_rest():
    assert near.near("reset", "rest") == True


def test_near_dragoon_dragon():
    assert near.near("dragoon", "dragon") == True


def test_near_eave_leave():
    assert near.near("eave", "leave") == False


def test_near_sleet_lets():
    assert near.near("sleet", "lets") == False


def test_near_two_less():
    assert near.near("sleet", "let") == False
