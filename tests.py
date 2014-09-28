import pytest
from convert import convert, BadInputValueException, ValueTooBigException
from constants import NUMBERS, MAGNITUDES, MAX

def test_negative_1():
    output = convert(-1)
    assert output == 'negative one'


def test_not_a_number():
    output = convert('not a number')
    assert output == BadInputValueException.message


def test_0():
    assert 'zero' == convert(0)


@pytest.mark.parametrize('number', xrange(1, 21))
def test_all_simple_numbers(number):
    assert number in NUMBERS


@pytest.mark.parametrize('number', xrange(1, 10))
def test_2_digits_multiples_of_10(number):
    assert number*10 in NUMBERS


def test_3():
    assert 'three' == convert(3)


def test_12():
    assert 'twelve' == convert(12)


def test_18():
    assert 'eighteen' == convert(18)


def test_21():
    assert 'twenty one' == convert(21)


def test_89():
    assert 'eighty nine' == convert(89)


def test_355():
    assert 'three hundred fifty five' == convert(355)


def test_1001():
    assert 'one thousand one' == convert(1001)


def test_999():
    assert 'nine hundred ninety nine' == convert(999)


def test_1000():
    assert 'one thousand' == convert(1000)


def test_1355():
    assert 'one thousand three hundred fifty five' == convert(1355)


def test_9999():
    assert 'nine thousand nine hundred ninety nine' == convert(9999)


def test_99000():
    assert 'ninety nine thousand' == convert(99000)


def test_99999():
    assert 'ninety nine thousand nine hundred ninety nine' == convert(99999)


@pytest.mark.parametrize('number', [MAX])
def test_max(number):
    groups = len(MAGNITUDES) * ['nine hundred ninety nine']
    output = []
    for idx, group in enumerate(groups, start=1):
        output.append(group)
        if groups[idx:]:
            output.append(MAGNITUDES[idx])
    output.reverse()
    assert ' '.join(output) == convert(number)


@pytest.mark.parametrize('number', [MAX+1])
def test_bigger_than_max(number):
    assert convert(number) == ValueTooBigException.message
