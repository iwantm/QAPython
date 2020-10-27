import pytest
from programs import grade_calc


def test_grade_calc_low_A():
    assert grade_calc.avg(
        70, 70, 70) == 'Your percentage score is: 70% \nYou scored a grade of: A'


def test_grade_calc_high_A():
    assert grade_calc.avg(
        100, 100, 100) == 'Your percentage score is: 100% \nYou scored a grade of: A'


def test_grade_calc_low_B():
    assert grade_calc.avg(
        60, 60, 60) == 'Your percentage score is: 60% \nYou scored a grade of: B'


def test_grade_calc_high_B():
    assert grade_calc.avg(
        69, 69, 69) == 'Your percentage score is: 69% \nYou scored a grade of: B'


def test_grade_calc_low_C():
    assert grade_calc.avg(
        50, 50, 50) == 'Your percentage score is: 50% \nYou scored a grade of: C'


def test_grade_calc_high_C():
    assert grade_calc.avg(
        59, 59, 59) == 'Your percentage score is: 59% \nYou scored a grade of: C'


def test_grade_calc_low_D():
    assert grade_calc.avg(
        40, 40, 40) == 'Your percentage score is: 40% \nYou scored a grade of: D'


def test_grade_calc_high_D():
    assert grade_calc.avg(
        49, 49, 49) == 'Your percentage score is: 49% \nYou scored a grade of: D'


def test_grade_calc_high_fail():
    assert grade_calc.avg(
        39, 39, 39) == 'You failed'


def test_grade_calc_low_fail():
    assert grade_calc.avg(
        0, 0, 0) == 'You failed'
