# FizzBuzz TDD Kata

Keepler FizzBuzz TDD Kata.

In this workshop we will implement FizzBuzz algorithm using the TDD development procedure. This is a incremental 
iterative procedure that consist on write a tests first, based on requirements, followed by the implementation of the 
minimum amount of code needed to that test to pass. Finally the procedure allow for a refactor of the code (source code
and test code) to eliminate redundancies, commit to higher standards, etc. 

The following image resume this process: 

![TDD](https://upload.wikimedia.org/wikipedia/commons/0/0b/TDD_Global_Lifecycle.png)

Also you can found documentation about this procedure [here](https://en.wikipedia.org/wiki/Test-driven_development)

<br />
<br />

## Current step

### Write a test that fails. 
From eleventh use case to fourteenth use case we did not implement any other test because we consider that all of them 
are already covered by the test cases we got. When comming to the fifteenth use case we got the first one that expects a
`FizzBuzz` word based on requirements. The tests fails. 

```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 5 items                                                                                   

test_fizz_buzz.py ....F                                                                       [100%]

============================================= FAILURES ==============================================
___________________________________ test_fizz_buzz_multiple_of_15 ___________________________________

    def test_fizz_buzz_multiple_of_15():
>       assert fizz_buzz(15) == "FizzBuzz"
E       AssertionError: assert 'Fizz' == 'FizzBuzz'
E         - Fizz
E         + FizzBuzz

test_fizz_buzz.py:28: AssertionError
==================================== 1 failed, 4 passed in 0.03s ====================================
``` 

### Write minimum code that make test pass.
We implement a new check just before multiple of 3 and multiple of 5 checks. This looks if the parameter is both 
multiple of 3 and 5 and in that case returns `FizzBuzz` word. We skip the more direct way of check if parameter is 15, 
cause we believe that with the work done until now  we have grasp some learning about the algorithm. 

```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 5 items                                                                                   

test_fizz_buzz.py .....                                                                       [100%]

========================================= 5 passed in 0.01s =========================================
```

<br />
<br />
<hr />

## Previous Steps

- [Step 1: Test environment](https://github.com/darofar/fizzbuzz_tdd/blob/3836e05c9f868c29cfb77241c703259afbd98d21/README.md)
- [Step 2: fizz_buzz(1)](https://github.com/darofar/fizzbuzz_tdd/blob/8ae70a62115a3ab44c30463d2da2e6b359c1f587/README.md)
- [Step 3: fizz_buzz(2)](https://github.com/darofar/fizzbuzz_tdd/blob/ba1d482ad49d06e414438b9f8983ed6a2ce251dd/README.md)
- [Step 4: fizz_buzz(3)](https://github.com/darofar/fizzbuzz_tdd/blob/0c449473984dd9d24de5969cc5b3f095963bd6b3/README.md)
- [Step 5: fizz_buzz(5)](https://github.com/darofar/fizzbuzz_tdd/blob/543513797610aaa2c5d9a11fb799fe7dd68b2676/README.md)
- [Step 6: fizz_buzz(6)](https://github.com/darofar/fizzbuzz_tdd/blob/2513a485b38a2a88036c524466a6332da361ff36/README.md)
