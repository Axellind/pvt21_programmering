# 1. Skriv en funktion som "vänder" en textsträng baklänges - utan att använda "reverse" (eller [::-1])!
# Använd istället strängar eller listor, och en for-loop.
# T.ex. "12345" blir "54321".
# 2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.
# 3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.
# t.ex.
# inrange(value=1, min=2, max=3) blir False eftersom 1 ligger utan för 2 till 3.
# inrange(value=10, min=0, max=100) blir True eftersom 10 ligger mellan 0 och 100.
import pytest


def rev_string(s):
    reversed_string = ''
    for c in s:
        reversed_string = c + reversed_string
    return reversed_string

print(rev_string('hejsan'))


def count_characters(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'
    count = 0
    for c in s:
        if c in alphabet:
            count += 1
    return count

print(count_characters('Hej Hej'))


def is_between(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False

print(is_between(1, 5, 10))
print(is_between(7, 5, 10))
print(is_between(-2, -5, 10))
print(is_between(6, 5, 10))




