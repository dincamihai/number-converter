#!/usr/bin/env python

import argparse
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

    def __init__(self, digits, position=None):
        self.digits = [Digit(value, idx) for idx, value in enumerate(digits)]
        self.position = position

    def in_words(self):
        words = []
        if self.digits and self.position:
            words.append(MAGNITUDES[self.position])
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

        self.digits = [d for d in reversed(unicode(self.value))]

    @property
    def break_points(self):
        return xrange(0, len(self.digits)+1, GROUP_SIZE)

    @property
    def groups(self):
        groups = []
        for idx, break_point in enumerate(self.break_points):
            group = DigitsGroup(
                self.digits[break_point:break_point+GROUP_SIZE], idx
            )
            if group.in_words():
                groups.append(group)
        return groups

    def in_words(self):
        words = []

        if self.value == 0:
            return 'zero'

        if self.value in NUMBERS:
            words.append(NUMBERS[self.value])
        else:
            for idx, group in enumerate(self.groups):
                words.append(group.in_words())

        if self.negative:
            words.append('negative')

        return ' '.join(reversed(words)).strip()


def main():
    parser = argparse.ArgumentParser(description='Convert number to words')
    parser.add_argument('number', metavar='N', type=int, help='an integer')

    options = parser.parse_args()

    result = Number(options.number).in_words()
    print(result.encode('utf-8'))


if __name__ == '__main__':
    main()
