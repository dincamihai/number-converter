#!/usr/bin/env python

import errors
from constants import NUMBERS, MAGNITUDES, GROUP_SIZE, MAX


class Digit(object):
    """ """

    def __init__(self, value, position=None):
        self.value = int(value)
        self.position = position
        self.multiplier = pow(10, (position or 0) % 2)

    def in_words(self):
        output = []
        if self.value:
            output.append(NUMBERS[self.value * self.multiplier])
            if self.position == 2:
                output.append(MAGNITUDES[0])
        return ' '.join(output)


class DigitsGroup(object):

    def __init__(self, digits):
        self.digits = [Digit(value, idx) for idx, value in enumerate(digits)]

    def in_words(self):
        words = []
        for digit in self.digits:
            if digit.in_words():
                words.append(digit.in_words())
        return ' '.join(reversed(words))


class Number(object):

    def __init__(self, value):
        self.value = value
        self.negative = value < 0

        if not type(self.value) == type(int()):
            raise errors.BadInputValueException
        if not self.value <= MAX:
            raise errors.ValueTooBigException

        if self.negative:
            self.value = -self.value

        self.words = []

    def in_words(self):
        if self.value == 0:
            return 'zero'

        if self.value in NUMBERS:
            self.words.append(NUMBERS[self.value])
        else:
            digits = [d for d in reversed(unicode(self.value))]
            break_points = xrange(0, len(digits)+1, GROUP_SIZE)

            for idx, break_point in enumerate(break_points, start=1):
                group = digits[break_point:break_point+GROUP_SIZE]
                if group:
                    self.words.append(DigitsGroup(group).in_words())
                    if digits[break_point+GROUP_SIZE:]:
                        self.words.append(MAGNITUDES[idx])

        if self.negative:
            self.words.append('negative')

        return ' '.join(reversed(self.words)).strip()
