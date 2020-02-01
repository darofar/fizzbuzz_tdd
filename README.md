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
Second use case test `fizz_buzz(2) = 2`. As current function always return `2` it will fails.

```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 3 items                                                                                   

test_fizz_buzz.py ..F                                                                         [100%]

============================================= FAILURES ==============================================
_________________________________________ test_fizz_buzz_2 __________________________________________

    def test_fizz_buzz_2():
>       assert fizz_buzz(2) == 2
E       assert 1 == 2
E        +  where 1 = fizz_buzz(2)

test_fizz_buzz.py:15: AssertionError
==================================== 1 failed, 2 passed in 0.02s ====================================
(.venv) darofar@tardis:~/workspace/keepler/tdd_katas/fizzbuzz_tdd$ 
``` 

### Write minimum code that make test pass.
Now function returns the same number received and complaint with both test cases. 
```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 3 items                                                                                   

test_fizz_buzz.py ...                                                                         [100%]

========================================= 3 passed in 0.01s =========================================
```

# Refactor 
Nothing to do. 

<br />
<br />
<hr />

## Previous Steps

- [Step 1: Test environment](https://github.com/darofar/fizzbuzz_tdd/blob/3836e05c9f868c29cfb77241c703259afbd98d21/README.md)
- [Step 2: fizz_buzz(1)](https://github.com/darofar/fizzbuzz_tdd/blob/8ae70a62115a3ab44c30463d2da2e6b359c1f587/README.md)

