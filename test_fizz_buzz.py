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


def test_fizz_buzz_6():
    assert fizz_buzz(6) == "Fizz"


def test_fizz_buzz_9():
    assert fizz_buzz(9) == "Fizz"


def test_fizz_buzz_10():
    assert fizz_buzz(10) == "Buzz"
