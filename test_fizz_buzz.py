from fizz_buzz import fizz_buzz


def test_environment():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 7


def test_fizz_buzz_n():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4


def test_fizz_buzz_multiple_of_3():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"


def test_fizz_buzz_multiple_of_5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"


def test_fizz_buzz_multiple_of_15():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
