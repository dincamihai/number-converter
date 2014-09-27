import string


NUMBERS = dict(
    zip(
        string.digits[1:],
        [
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ]
    )
)

for key, value in NUMBERS.items():
    NUMBERS[unicode(int(key)+10)] = '%steen' % value
    NUMBERS[unicode(int(key)*10)] = '%sty' % value

NUMBERS.update(dict([
    ('11', 'eleven'),
    ('12', 'twelve'),
    ('13', 'thirteen'),
    ('15', 'fifteen'),
    ('18', 'eighteen'),

]))

NUMBERS.update(dict([
    ('0', 'zero'),
    ('10', 'ten'),
    ('20', 'twenty'),
    ('30', 'thirty'),
    ('50', 'fifty'),
    ('80', 'eighty'),
]))
