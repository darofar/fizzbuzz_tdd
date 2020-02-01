from fizz_buzz import fizz_buzz


def test_environment():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 7


def test_fizz_buzz_n():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4


def test_fizz_buzz_3():
    assert fizz_buzz(3) == "Fizz"


def test_fizz_buzz_5():
    assert fizz_buzz(5) == "Buzz"
