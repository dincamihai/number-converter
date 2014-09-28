from constants import MAX


class BadInputValueException(Exception):
    message = 'value needs to be an integer'


class ValueTooBigException(Exception):
    message = (
        'You need to extend constants.MAGNITUDES list or '
        'pass-in a value <= %s' % MAX
    )
