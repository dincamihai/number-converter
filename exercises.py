#!/usr/bin/env python

import pytest
from constants import NUMBERS, MAGNITUDES


MIN = 0
MAX = 999999


class BadInputValueException(Exception):
    """ raised when value is not in the allowed interval """

    message = 'value needs to be an integer between %s and %s' % (MIN, MAX)


class NumberConverter(object):

    def __init__(self, value):
        if not MIN <= value <= MAX:
            raise BadInputValueException

        self.value = value

    def in_words(self):
        words = []
        if self.value in NUMBERS:
            return NUMBERS[self.value]
        else:
            digits = [d for d in unicode(self.value)]
            for idx, digit_value in enumerate(digits, start=1):
                if digit_value == '0':
                    continue
                magnitude = pow(10, len(digits)-idx)
                digit_value = int(digit_value)
                if magnitude < 100:
                    digit_value = int(digit_value) * magnitude
                words.append(NUMBERS[digit_value])
                if magnitude in MAGNITUDES:
                    words.append(MAGNITUDES[magnitude])
        return ' '.join(words)


def convert(value):
    try:
        return NumberConverter(value).in_words()
    except BadInputValueException as exc:
        return exc.message


def test_negative_1():
    output = convert(-1)
    assert output == BadInputValueException.message


def test_a():
    output = convert('not a number')
    assert output == BadInputValueException.message


def test_MIN():
    assert 'zero' == convert(MIN)


@pytest.mark.parametrize('number', xrange(MIN, 21))
def test_all_simple_numbers(number):
    assert number in NUMBERS


@pytest.mark.parametrize('number', xrange(1, 10))
def test_2_digits_multiples_of_10(number):
    assert number*10 in NUMBERS


def test_3():
    assert 'three' == convert(3)


def test_12():
    assert 'twelve' == convert(12)


def test_18():
    assert 'eighteen' == convert(18)


def test_21():
    assert 'twenty one' == convert(21)


def test_89():
    assert 'eighty nine' == convert(89)


def test_355():
    assert 'three hundred fifty five' == convert(355)


def test_1001():
    assert 'one thousand one' == convert(1001)


def test_1355():
    assert 'three hundred fifty five' == convert(355)


def test_1000():
    assert 'one thousand' == convert(1000)


def test_9999():
    assert 'nine thousand nine hundred ninety nine' == convert(9999)


@pytest.mark.xfail
def test_99999():
    assert 'ninety nine thousand nine hundred ninety nine' == convert(99999)


@pytest.mark.xfail
def test_MAX():
    assert 'nine hundred ninety nine thousand nine hundred ninety nine' == convert(MAX)
