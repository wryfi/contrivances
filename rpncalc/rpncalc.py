# -*- coding: utf-8 -*-

from decimal import Decimal
import re
from math import sqrt
import sys


def main(expression):
  if not re.match(r'^-*\d+\.{0,1}\d*\s[\s0-9*/+^√-]+', expression):
    raise SystemExit('Error: RPN expressions can only contain numbers and operators.')
  try:
    expression = ReversePolishNotationExpression(expression)
    print(expression.calculate())
  except RuntimeError as error:
    raise SystemExit(error)


class ReversePolishNotationExpression(object):
  def __init__(self, expression):
    self.calculationExpressions = {
        '√' : lambda x: Decimal(sqrt(x)),
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y,
        '^' : lambda x, y: x ** y,
    }
    self.expression = expression

  def _parseExpression(self):
    elements, parsed = [], re.split(r'\s+', self.expression)
    for component in parsed:
      if re.match(r'^-*\d+\.{0,1}\d*$', component):
        elements.append(Decimal(component))
      elif component in self.calculationExpressions.keys():
        elements.append(component)
      else:
        raise SyntaxError('"%s" is neither an operator nor a decimal number' % (component,))
    return elements

  def calculate(self):
    stack = []
    for element in self._parseExpression():
      if type(element) is Decimal:
        stack.append(element)
      else:
        operands = [stack.pop()]
        if element != '√':
          if len(stack) < 1:
            raise RuntimeError('There were not enough operands in the expression.')
          operands.insert(0, stack.pop())
        stack.append(self.calculationExpressions.get(element)(*operands))
    if len(stack) > 1:
      raise RuntimeError('There were not enough operators in the expression.')
    return round(stack.pop(), 2)


if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise SystemExit('Specify an RPN expression in quotes.')
  main(sys.argv[1])
