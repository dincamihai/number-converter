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

    is_null = False

    def __init__(self, digits, position=None):
        self.digits = []
        digits = digits[::-1].zfill(3)
        if digits == '000':
            self.is_null = True
        self.digits.append(Digit(int(digits[0]), 2))
        if digits[1] == '1':
            self.digits.append(Digit(int(digits[1:])))
        else:
            self.digits.append(Digit(int(digits[1]), 1))
            self.digits.append(Digit(int(digits[2])))
        self.position = position

    def in_words(self):
        words = [d.in_words() for d in self.digits if d.value]
        if self.digits and not self.is_null and self.position:
            words.append(MAGNITUDES[self.position])
        return ' '.join(words)


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

        self.digits = unicode(self.value)[::-1]

    @property
    def break_points(self):
        return xrange(0, len(self.digits)+1, GROUP_SIZE)

    @property
    def groups(self):
        groups = []
        for idx, break_point in enumerate(self.break_points):
            digits = self.digits[break_point:break_point+GROUP_SIZE]
            if digits:
                groups.append(DigitsGroup(digits, idx))
        return groups

    def in_words(self):
        if self.value == 0:
            return 'zero'

        words = [g.in_words() for g in self.groups if not g.is_null]

        if self.negative:
            words.append('negative')

        return ' '.join(reversed(words)).strip()


def main():
    parser = argparse.ArgumentParser(description='Convert number to words')
    parser.add_argument('number', metavar='N', type=int, help='an integer')

    options = parser.parse_args()

    try:
        result = Number(options.number).in_words()
        print(result.encode('utf-8'))
    except errors.ValueTooBigException as exc:
        print (exc.message)


if __name__ == '__main__':
    main()
