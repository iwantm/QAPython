import pytest
from programs import num2words_manual


def test_num2words_manual_hun():
    assert num2words_manual.to_word(123) == 'one hundred and twenty three'


def test_num2words_manual_thou():
    assert num2words_manual.to_word(5011) == 'five thousand and eleven'


def test_num2words_manual_big():
    assert num2words_manual.to_word(
        923341573943234) == 'nine hundred and twenty three trillion, three hundred and forty one billion, five hundred and seventy three million, nine hundred and forty three thousand, two hundred and thirty four'
