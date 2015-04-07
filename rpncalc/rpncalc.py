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
    self.elements = self._parseExpression()
    self.stack = []

  def _parseExpression(self):
    elements = []
    parsed = re.split(r'\s+', self.expression)
    for component in parsed:
      if re.match(r'^-*\d+\.{0,1}\d*$', component):
        elements.append(Decimal(component))
      elif component in self.calculationExpressions.keys():
        elements.append(component)
      else:
        raise RuntimeError('"%s" is neither an operator nor a decimal number' % (component,))
    return elements

  def calculate(self):
    for element in self.elements:
      if type(element) is Decimal:
        self.stack.append(element)
      else:
        if len(self.stack) < 2 and element != '√':
          raise RuntimeError('There were not enough operands in the expression.')
        operands = [self.stack.pop()]
        if element != '√':
          operands.insert(0, self.stack.pop())
        result = self.calculationExpressions.get(element)(*operands)
        self.stack.append(result)
    if len(self.stack) > 1:
      raise RuntimeError('There were not enough operators in the expression.')
    return round(self.stack.pop(), 2)


if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise SystemExit('Specify an RPN expression in quotes.')
  main(sys.argv[1])
