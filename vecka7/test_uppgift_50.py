from uppgift_49 import rev_string, count_characters, is_between
import pytest

def test_rev():
    assert rev_string('123') == '321'