import string


NUMBERS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


for key, value in NUMBERS.items():
    NUMBERS[key+10] = '%steen' % value
    NUMBERS[key*10] = '%sty' % value


NUMBERS.update(dict([
    (11, 'eleven'),
    (12, 'twelve'),
    (13, 'thirteen'),
    (15, 'fifteen'),
    (18, 'eighteen'),

]))


NUMBERS.update(dict([
    (10, 'ten'),
    (20, 'twenty'),
    (30, 'thirty'),
    (50, 'fifty'),
    (80, 'eighty'),
]))


MAGNITUDES = ['hundred', 'thousand', 'million']


MAX = pow(10, len(MAGNITUDES) * 3) - 1
