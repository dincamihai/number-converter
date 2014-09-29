from constants import MAX
from convert import Number


class BadInputValueException(Exception):
    message = 'value needs to be an integer'


class ValueTooBigException(Exception):
    message = (
        "You need to extend constants.MAGNITUDES list or "
        "pass-in a value smaller or equal to:\n"
        "%s" % Number(MAX).in_words()
    )
