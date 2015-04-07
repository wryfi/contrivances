# rpncalc

## About

rpncalc is a simple python module for evaluating mathematical expressions in
Reverse-Polish Notation (RPN), including rudimentary decimal support.

### Original Assignment

This was an at-home assignment for an interview:

> Implement a RPN evaluator in your language of choice. It should be able to 
> evaluate the following strings and answer with the corresponding numbers:
> 
> * “1 2 +” = 3
> * “4 2 /” = 2
> * “2 3 4 + *” = 14
> * “3 4 + 5 6 + *” = 77
> * “13 4 -” = 9
> 
> And should provide an error message for the following types of errors
> 
> * “1 +” (not enough arguments)
> * “a b +” (invalid number)
> 
> We should be able to evaluate a string from the command line in the following
> way. For example, if you choose to use Ruby, invoking it might look like:
> 
> ```
> $ ruby rpn.rb "1 2 +"
> ```

I added support for decimals, negatives, exponents, and square roots.

## Requirements

rpncalc has been developed against Python 3.4 and additionally tested against
Python 2.7. Other python versions may work, but use at your own risk. Only the
standard python libraries are required.


## Usage

You can use rpncalc programatically or from the shell.

### shell usage

```
$ python rpncalc.py "1 1 +"
2
```

### programmatic usage

```
from rpncalc import ReversePolishNotationExpression
expression = ReversePolishNotationExpression('1 1 +')
print(expression.calculate())
2
```

## Tests

Tests representing the requirements specified in the assignment are in the
tests module. To run the tests, simply execute `python tests.py -v`. The test
suite assumes that it is in the same directory as `rpncalc.py`.
