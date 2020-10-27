import pytest
import mock
import builtins
from programs import num2words_library


def test_num2words_library_hun():
    with mock.patch.object(builtins, 'input', lambda _: '123'):
        assert num2words_library.n2w_lib() == 'one hundred and twenty-three'


def test_num2words_library_thou():
    with mock.patch.object(builtins, 'input', lambda _: '5011'):
        assert num2words_library.n2w_lib() == 'five thousand and eleven'


def test_num2words_library_big():
    with mock.patch.object(builtins, 'input', lambda _: '923341573943234'):
        assert num2words_library.n2w_lib() == 'nine hundred and twenty-three trillion, three hundred and forty-one billion, five hundred and seventy-three million, nine hundred and forty-three thousand, two hundred and thirty-four'
