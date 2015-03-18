# rpncalc

rpncalc is a simple python module for evaluating mathematical expressions in
Reverse-Polish Notation (RPN), including rudimentary decimal support.

## requirements

rpncalc has been developed against Python 3.4 and additionally tested against
Python 2.7. Other python versions may work, but use at your own risk. Only the
standard python libraries are required.


## usage

You can use rpncalc programatically or from the shell.

### shell usage

```
$ python rpncalc.py "1 1 +"
2
```

### programmatic usage

```
from rpncalc import calculator
print(calculator('1 1 +'))
2
```

## tests

Tests representing the requirements specified in the assignment are in the
tests module. To run the tests, simply execute `python tests.py -v`. The test
suite assumes that it is in the same directory as `rpncalc.py`.

## limitations

* Not all expression syntax errors are caught (e.g. missing spaces such as `1
1+`).  
* Python packaging not included.
* Argument handling/help-text for shell invocation could be improved.
