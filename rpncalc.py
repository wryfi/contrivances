from decimal import Decimal
import logging
import re
import sys


logging.basicConfig(
    format='%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


def main(expression):
  if not re.match(r'[0-9*/+-]+', expression):
    raise SystemExit('Error: RPN expressions can only contain numbers and operators.')
  try:
    print(calculator(expression))
  except RuntimeError as error:
    raise SystemExit(error)


def calculator(expression):
  '''
  Takes a Reverse Polish Notation expression as a string and returns the result.
  '''
  calculationExpressions = {
      '+' : lambda x, y : x + y,
      '-' : lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '^': lambda x, y: x**y
  }
  parsed = re.split(r'\s+', expression)
  logging.debug(parsed)
  elements = []
  for component in parsed:
    # processing below does not check for missing spaces
    if re.match(r'^\d*\.*\d+$', component):
      elements.append(Decimal(component))
    elif component in calculationExpressions.keys():
      elements.append(component)
  logging.debug(elements)
  stack = []
  for element in elements:
    if type(element) is Decimal:
      stack.append(element)
    else:
      if len(stack) < 2:
        raise RuntimeError('There were not enough operands in the expression.')
      else:
        operands = [stack.pop()]
        operands.insert(0, stack.pop())
        result = calculationExpressions.get(element)(operands[0], operands[1])
        stack.append(result)
  if len(stack) > 1:
    raise RuntimeError('There were not enough operators in the expression.')
  logging.debug(stack)
  return stack.pop()


if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise SystemExit('Specify an RPN expression in quotes.')
  main(sys.argv[1])
