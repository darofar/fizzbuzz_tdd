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
Testing the fourth use case we got that for the first time a test directly passes `fizz_buzz(4) = 4`. This case is 
already dealt with in the code. So we are just added to this step ass per TDD procedure, keep testing until you find a 
test that fails. 

The fifth use case fails cause it expects a result that have not been implemented yet: `fizz_buzz(5) = "Buzz"`. 

```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 6 items                                                                                   

test_fizz_buzz.py .....F                                                                      [100%]

============================================= FAILURES ==============================================
_________________________________________ test_fizz_buzz_5 __________________________________________

    def test_fizz_buzz_5():
>       assert fizz_buzz(5) == "Buzz"
E       AssertionError: assert 5 == 'Buzz'
E        +  where 5 = fizz_buzz(5)

test_fizz_buzz.py:27: AssertionError
==================================== 1 failed, 5 passed in 0.03s ====================================
``` 

<br />
<br />
<hr />

## Previous Steps

- [Step 1: Test environment](https://github.com/darofar/fizzbuzz_tdd/blob/3836e05c9f868c29cfb77241c703259afbd98d21/README.md)
- [Step 2: fizz_buzz(1)](https://github.com/darofar/fizzbuzz_tdd/blob/8ae70a62115a3ab44c30463d2da2e6b359c1f587/README.md)
- [Step 3: fizz_buzz(2)](https://github.com/darofar/fizzbuzz_tdd/blob/ba1d482ad49d06e414438b9f8983ed6a2ce251dd/README.md)
- [Step 4: fizz_buzz(3)](https://github.com/darofar/fizzbuzz_tdd/blob/0c449473984dd9d24de5969cc5b3f095963bd6b3/README.md)