from fizz_buzz import fizz_buzz


def test_environment():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 7


def test_fizz_buzz_1():
    assert fizz_buzz(1) == 1
