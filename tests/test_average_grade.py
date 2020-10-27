import pytest
from programs import average_grade


def test_average_grade_high_A():
    assert average_grade.grade('Iwan', 25, 50, 100) == (
        'Iwan achieved 100%. Final grade: A')


def test_average_grade_low_A():
    assert average_grade.grade('Iwan', 18, 35, 70) == (
        'Iwan achieved 70%. Final grade: A')


def test_average_grade_high_B():
    assert average_grade.grade('Iwan', 18, 34, 69) == (
        'Iwan achieved 69%. Final grade: B')


def test_average_grade_low_B():
    assert average_grade.grade('Iwan', 15, 30, 60) == (
        'Iwan achieved 60%. Final grade: B')


def test_average_grade_high_C():
    assert average_grade.grade('Iwan', 15, 29, 59) == (
        'Iwan achieved 59%. Final grade: C')


def test_average_grade_low_C():
    assert average_grade.grade('Iwan', 13, 25, 50) == (
        'Iwan achieved 50%. Final grade: C')


def test_average_grade_high_D():
    assert average_grade.grade('Iwan', 13, 24, 49) == (
        'Iwan achieved 49%. Final grade: D')


def test_average_grade_low_D():
    assert average_grade.grade('Iwan', 10, 20, 40) == (
        'Iwan achieved 40%. Final grade: D')


def test_average_grade_high_fail():
    assert average_grade.grade('Iwan', 10, 20, 39) == (
        'Iwan Failed. Final percentage: 39%')


def test_average_grade_low_fail():
    assert average_grade.grade('Iwan', 0, 0, 0) == (
        'Iwan Failed. Final percentage: 0%')
