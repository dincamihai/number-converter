#!/usr/bin/env python

from constants import NUMBERS


class BadInputValueException(Exception):
    """ raised when value is not in the allowed interval """


class NumberConverter(object):

    def __init__(self, value):
        if not 0 <= value <= 1000:
            message = 'value needs to be an integer between 0 and 1000'
            raise BadInputValueException, message

        self.value = unicode(value)

    def in_words(self):
        words = []
        if self.value in NUMBERS:
            return NUMBERS[self.value]
        else:
            digits = [d for d in self.value]
            for idx, digit_value in enumerate(digits, start=1):
                digit_value = unicode(
                    int(digit_value) * pow(10, len(digits)-idx)
                )
                words.append(NUMBERS[digit_value])
        return ' '.join(words)


def convert(value):
    try:
        return NumberConverter(value).in_words()
    except BadInputValueException as exc:
        return exc.message


def test_negative_1():
    output = convert(-1)
    assert output == 'value needs to be an integer between 0 and 1000'

def test_1001():
    output = convert(1001)
    assert output == 'value needs to be an integer between 0 and 1000'

def test_a():
    output = convert('not a number')
    assert output == 'value needs to be an integer between 0 and 1000'

def test_0():
    assert 'zero' == convert(0)

def test_3():
    assert 'three' == convert(3)

def test_12():
    assert 'twelve' == convert(12)

def test_18():
    assert 'eighteen' == convert(18)

def test_20():
    assert 'twenty' == convert(20)

def test_21():
    assert 'twenty one' == convert(21)

def test_89():
    assert 'eighty nine' == convert(89)

def test_90():
    assert 'ninety' == convert(90)
