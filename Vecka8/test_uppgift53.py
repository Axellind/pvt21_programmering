import pytest
from uppgift53 import factors


def test_factors_known_numbers():
    assert factors(36) == [2, 2, 3, 3]
    assert factors(500000) == [2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]


def test_factors_prime_17():
    assert factors(17) == [17]


def test_factors_odd_numbers():
    assert factors(77) == [7, 11]
    # assert factors()