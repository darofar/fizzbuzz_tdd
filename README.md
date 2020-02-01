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
This test is meant to test the first use case for FizzBuzz algorithm. That `fizz_buzz(1) = 1`. It fails because a 
function named `fizz_buzz` did not exists. 

```
$> python -m pytest test_fizz_buzz.py 
==========================================================
    def test_fizz_buzz_1():
>       assert fizz_buzz(1) == 1
E       NameError: name 'fizz_buzz' is not defined

test_fizz_buzz.py:7: NameError
==========================================================
```

### Write minimum code that make test pass. 
- Create a new module `fizz_buzz` with a function defined `fizz_buzz`that receives a parameter and always return 1. 

```
python -m pytest test_fizz_buzz.py 
======================================== test session starts ========================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/darofar/workspace/keepler/tdd_katas/fizzbuzz_tdd
collected 2 items                                                                                   

test_fizz_buzz.py ..                                                                          [100%]

========================================= 2 passed in 0.01s =========================================
```

<br />
<br />
<hr />

## First Step

### Write a test that fails. 
This test is meant to test properly configured environment with python 3.7 as project interpreter. 

```
$> python -m pytest test_fizz_buzz 
/usr/bin/python: No module named pytest
```
### Write minimum code that make test pass. 
- Created a virtual environment with python 3.7 as interpreter. 
```
virtualenv -p /usr/bin/python3.7 .venv
```
- Added a requirements.txt file with `pytest` dependency. Install dependencies. 
```
source .venv/bin/activate
pip install -r requirements.txt
```

### Refactor code
- Added a `.gitignore` file to avoid IDE and cache files to be added to the repository. 
``` 
#.gitignore
.idea
.pytest_cache
__pycache__
```
