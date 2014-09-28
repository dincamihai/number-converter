import pytest
from convert import (
    BadInputValueException, ValueTooBigException,
    Digit, Number
)
from constants import NUMBERS, MAGNITUDES, MAX


class TestNumberConverter(object):

    def test_negative_1(self):
        output = Number(-1).in_words()
        assert output == 'negative one'

    def test_not_a_number(self):
        output = Number('not a number').in_words()
        assert output == BadInputValueException.message

    def test_0(self):
        assert 'zero' == Number(0).in_words()

    @pytest.mark.parametrize('number', xrange(1, 21))
    def test_all_simple_numbers(self, number):
        assert number in NUMBERS

    @pytest.mark.parametrize('number', xrange(1, 10))
    def test_2_digits_multiples_of_10(self, number):
        assert number*10 in NUMBERS

    def test_3(self):
        assert 'three' == Number(3).in_words()

    def test_12(self):
        assert 'twelve' == Number(12).in_words()

    def test_18(self):
        assert 'eighteen' == Number(18).in_words()

    def test_21(self):
        assert 'twenty one' == Number(21).in_words()

    def test_89(self):
        assert 'eighty nine' == Number(89).in_words()

    def test_355(self):
        assert 'three hundred fifty five' == Number(355).in_words()

    def test_1001(self):
        assert 'one thousand one' == Number(1001).in_words()

    def test_999(self):
        assert 'nine hundred ninety nine' == Number(999).in_words()

    def test_1000(self):
        assert 'one thousand' == Number(1000).in_words()

    def test_1355(self):
        assert 'one thousand three hundred fifty five' == Number(1355).in_words()

    def test_9999(self):
        assert 'nine thousand nine hundred ninety nine' == Number(9999).in_words()

    def test_99000(self):
        assert 'ninety nine thousand' == Number(99000).in_words()

    def test_99999(self):
        assert 'ninety nine thousand nine hundred ninety nine' == Number(99999).in_words()

    @pytest.mark.parametrize('number', [MAX])
    def test_max(self, number):
        groups = len(MAGNITUDES) * ['nine hundred ninety nine']
        output = []
        for idx, group in enumerate(groups, start=1):
            output.append(group)
            if groups[idx:]:
                output.append(MAGNITUDES[idx])
        output.reverse()
        assert ' '.join(output) == Number(number).in_words()

    @pytest.mark.parametrize('number', [MAX+1])
    def test_bigger_than_max(self, number):
        assert Number(number).in_words() == ValueTooBigException.message


class TestConvertDigit(object):

    def test_convert_digit(self):
        digit = Digit(1)
        assert digit.in_words() == 'one'

    def test_convert_zero_digit(self):
        digit = Digit(0)
        assert digit.in_words() == ''

    def test_convert_digit_with_position(self):
        digit = Digit(1, position=1)
        assert digit.in_words() == 'ten'
