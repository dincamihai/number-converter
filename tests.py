import pytest
from convert import (
    convert, BadInputValueException, ValueTooBigException,
    Digit
)
from constants import NUMBERS, MAGNITUDES, MAX


class TestNumberConverter(object):

    def test_negative_1(self):
        output = convert(-1)
        assert output == 'negative one'

    def test_not_a_number(self):
        output = convert('not a number')
        assert output == BadInputValueException.message

    def test_0(self):
        assert 'zero' == convert(0)

    @pytest.mark.parametrize('number', xrange(1, 21))
    def test_all_simple_numbers(self, number):
        assert number in NUMBERS

    @pytest.mark.parametrize('number', xrange(1, 10))
    def test_2_digits_multiples_of_10(self, number):
        assert number*10 in NUMBERS

    def test_3(self):
        assert 'three' == convert(3)

    def test_12(self):
        assert 'twelve' == convert(12)

    def test_18(self):
        assert 'eighteen' == convert(18)

    def test_21(self):
        assert 'twenty one' == convert(21)

    def test_89(self):
        assert 'eighty nine' == convert(89)

    def test_355(self):
        assert 'three hundred fifty five' == convert(355)

    def test_1001(self):
        assert 'one thousand one' == convert(1001)

    def test_999(self):
        assert 'nine hundred ninety nine' == convert(999)

    def test_1000(self):
        assert 'one thousand' == convert(1000)

    def test_1355(self):
        assert 'one thousand three hundred fifty five' == convert(1355)

    def test_9999(self):
        assert 'nine thousand nine hundred ninety nine' == convert(9999)

    def test_99000(self):
        assert 'ninety nine thousand' == convert(99000)

    def test_99999(self):
        assert 'ninety nine thousand nine hundred ninety nine' == convert(99999)

    @pytest.mark.parametrize('number', [MAX])
    def test_max(self, number):
        groups = len(MAGNITUDES) * ['nine hundred ninety nine']
        output = []
        for idx, group in enumerate(groups, start=1):
            output.append(group)
            if groups[idx:]:
                output.append(MAGNITUDES[idx])
        output.reverse()
        assert ' '.join(output) == convert(number)

    @pytest.mark.parametrize('number', [MAX+1])
    def test_bigger_than_max(self, number):
        assert convert(number) == ValueTooBigException.message


class TestConvertDigit(object):

    def test_convert_digit(self):
        digit = Digit(1)
        assert digit.in_words() == 'one'

    def test_convert_zero_digit(self):
        digit = Digit(0)
        assert digit.in_words() == 'zero'

    def test_convert_digit_with_position(self):
        digit = Digit(1, position=1)
        assert digit.in_words() == 'ten'
