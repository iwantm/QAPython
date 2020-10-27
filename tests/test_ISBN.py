import pytest
from programs import ISBN


def test_ISBN():
    assert ISBN.ld('978-0-306-40615') == '978-0-306-40615-7'
