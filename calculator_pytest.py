import pytest

from calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('6-3') == 3


def test_multiply():
    assert calculator('7*8') == 56


def test_devide():
    assert calculator('25/5') == 5


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('qwert')
    assert 'The expression must contain at least one sign (+-/*)' == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('5+3-8')
    assert 'Expression must contain 2 integers and 1 sign' == error.value.args[0]


def test_no_int():
    with pytest.raises(ValueError) as error:
        calculator('5.6+6')
    assert 'Expression must contain 2 integers and 1 sign' == error.value.args[0]


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as error:
        calculator('15/0')
    assert 'Division by zero is not allowed' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
