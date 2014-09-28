#!/usr/bin/env python

from constants import NUMBERS, MAGNITUDES, MAX


GROUP_SIZE = 3


class BadInputValueException(Exception):
    """ raised when value is not in the allowed interval """

    message = 'value needs to be an integer'


class ValueTooBigException(Exception):
    """ raised when value is not in the allowed interval """

    message = (
        'You need to extend constants.MAGNITUDES list or '
        'pass-in a value <= %s' % MAX
    )


class ThreeDigitsGroup(object):

    def __init__(self, value):
        self.value = value
        self.digits = [d for d in unicode(self.value)]

    def in_words(self):
        words = []
        if self.value in NUMBERS:
            return NUMBERS[self.value]
        else:
            for idx, digit in enumerate(self.digits, start=1):
                if digit == '0':
                    continue
                no_of_zeros = len(self.digits)-idx
                multiplier = pow(10, no_of_zeros % 3)
                digit = int(digit)
                if multiplier == 10:
                    digit = int(digit) * multiplier
                words.append(NUMBERS[digit])
                if multiplier == 100:
                    words.append(MAGNITUDES[0])
        return ' '.join(words)


def convert(value):

    if not type(value) == type(int()):
        return BadInputValueException.message
    if not value <= MAX:
        return ValueTooBigException.message

    output = []
    negative = False

    if value == 0:
        return 'zero'
    elif value < 0:
        negative = True
        value = -value

    digits = [d for d in unicode(value)]
    digits.reverse()

    break_points = range(0, len(digits)+1, GROUP_SIZE)

    for idx, break_point in enumerate(break_points, start=1):
        group = digits[break_point:break_point+GROUP_SIZE]
        if group:
            group.reverse()
            group = int(''.join(group))
            output.append(ThreeDigitsGroup(group).in_words())
            if digits[break_point+GROUP_SIZE:]:
                output.append(MAGNITUDES[idx])

    if negative:
        output.append('negative')

    output.reverse()
    return ' '.join(output).strip()
