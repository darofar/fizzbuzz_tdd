# FizzBuzz TDD Kata

Keepler FizzBuzz TDD Kata.

In this workshop we will implement FizzBuzz algorithm using the TDD development procedure. This is a incremental 
iterative procedure that consist on write a tests first, based on requirements, followed by the implementation of the 
minimum amount of code needed to that test to pass. Finally the procedure allow for a refactor of the code (source code
and test code) to eliminate redundancies, commit to higher standards, etc. 

The following image resume this process: 

![TDD](https://upload.wikimedia.org/wikipedia/commons/0/0b/TDD_Global_Lifecycle.png =750x)

Also you can found documentation about this procedure [here](https://en.wikipedia.org/wiki/Test-driven_development)

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
```