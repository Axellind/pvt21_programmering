import pytest
from uppgift15 import *

ny_text = "Hejsan detta är en text"


def test_count_vokaler():
    assert count_vokaler(text) == 7

#def test_count_letters_and_digits():
#    assert countLetterAndDigits(ny_text) ==