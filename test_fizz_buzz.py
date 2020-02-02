from fizz_buzz import fizz_buzz

FIZZBUZZ_NUMBERS = [i for i in range(15, 100, 15)]
FIZZ_NUMBERS = [i for i in range(3, 100, 3) if i not in FIZZBUZZ_NUMBERS]
BUZZ_NUMBERS = [i for i in range(5, 100, 5) if i not in FIZZBUZZ_NUMBERS]
OTHER_NUMBERS = [i for i in range(1, 100) if i not in FIZZ_NUMBERS and i not in BUZZ_NUMBERS and i not in FIZZBUZZ_NUMBERS]


def test_environment():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 7


def test_fizz_buzz_n():
    for n in OTHER_NUMBERS:
        assert fizz_buzz(n) == n


def test_fizz_buzz_multiple_of_3():
    for n in FIZZ_NUMBERS:
        assert fizz_buzz(n) == "Fizz"


def test_fizz_buzz_multiple_of_5():
    for n in BUZZ_NUMBERS:
        assert fizz_buzz(n) == "Buzz"


def test_fizz_buzz_multiple_of_15():
    for n in FIZZBUZZ_NUMBERS:
        assert fizz_buzz(n) == "FizzBuzz"
