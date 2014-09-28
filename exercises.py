#!/usr/bin/env python

import pytest
from constants import NUMBERS, MAGNITUDES


MIN = 0
MAX = 999999


class BadInputValueException(Exception):
    """ raised when value is not in the allowed interval """

    message = 'value needs to be an integer between %s and %s' % (MIN, MAX)


class ThreeDigitsNumber(object):

    def __init__(self, value):
        self.value = value

    def in_words(self):
        words = []
        if self.value in NUMBERS:
            return NUMBERS[self.value]
        else:
            digits = [d for d in unicode(self.value)]
            for idx, digit in enumerate(digits, start=1):
                if digit == '0':
                    continue
                no_of_zeros = len(digits)-idx
                multiplier = pow(10, no_of_zeros % 3)
                digit = int(digit)
                if multiplier == 10:
                    digit = int(digit) * multiplier
                words.append(NUMBERS[digit])
                if multiplier == 100:
                    words.append(MAGNITUDES[multiplier])
        return ' '.join(words)


def convert(value):
    GROUP_SIZE = 3
    if not MIN <= value <= MAX:
        return BadInputValueException.message

    digits = [d for d in unicode(value)]
    digits.reverse()
    output = []
    if value == 0:
        return 'zero'

    break_points = range(0, len(digits)+1, GROUP_SIZE)

    for idx, break_point in enumerate(break_points, start=1):
        group = digits[break_point:break_point+GROUP_SIZE]
        if group:
            group.reverse()
            group = int(''.join(group))
            output.append(ThreeDigitsNumber(group).in_words())
            if digits[break_point+GROUP_SIZE:]:
                output.append(MAGNITUDES.get(idx, ''))

    output.reverse()
    return ' '.join(output).strip()


def test_negative_1():
    output = convert(-1)
    assert output == BadInputValueException.message


def test_not_a_number():
    output = convert('not a number')
    assert output == BadInputValueException.message


def test_MIN():
    assert 'zero' == convert(MIN)


@pytest.mark.parametrize('number', xrange(1, 21))
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
    assert 'one thousand three hundred fifty five' == convert(1355)


def test_1000():
    assert 'one thousand' == convert(1000)


def test_999():
    assert 'nine hundred ninety nine' == convert(999)


def test_9999():
    assert 'nine thousand nine hundred ninety nine' == convert(9999)


def test_99000():
    assert 'ninety nine thousand' == convert(99000)


def test_99999():
    assert 'ninety nine thousand nine hundred ninety nine' == convert(99999)


def test_MAX():
    assert 'nine hundred ninety nine thousand nine hundred ninety nine' == convert(MAX)
