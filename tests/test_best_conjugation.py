import pytest
import os
from programs import best_conjugation


def test_best_conjugation_dict():
    script_dir = os.path.dirname(__file__)
    rel_path = "wordlist.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    text_file = open(os.path.join(abs_file_path), "r")
    words = text_file.read().split("\n")
    assert best_conjugation.dictionary() == words


def test_best_conjugation_sub():
    assert best_conjugation.sub(
        'test') == ['t', 'te', 'tes', 'test', 'e', 'es', 'est', 's', 'st', 't']


def test_best_conjugation_bc():
    assert best_conjugation.bc('test') == [
        't', 'te', 'e', 'es', 'est', 's', 'st']
