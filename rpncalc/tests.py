from decimal import Decimal
import os
import subprocess
import unittest


TEST_EXPRESSIONS = [
    ('expr_one_plus_two', '1 2 +', '3'),
    ('expr_four_over_two', '4 2 /', '2'),
    ('expr_thirteen_minus_four', '13 4 -', '9'),
    ('expr_negative_one_plus_one', '-1 1 +', '0'),
    ('expr_add_multiply_three_operands', '2 3 4 + *', '14'),
    ('expr_add_multiply_two_pair_operands', '3 4 + 5 6 + *', '77'),
    ('expr_three_plus_radical_four', '3 4 √ +', '5'), 
    ('expr_basketball_volume_cm', '25 2 / 3 ^ 3.14159 * 4 3 / *', '8181.22'),
    ('expr_earth_volume_mi', '7918 2 / 3 ^ 3.14159 * 4 3 / *', '259923022015.94'),
]


class RpnTest(unittest.TestCase):

  def test_can_import_rpncalc(self):
    '''
    Tests that we can import the expression class from rpcncalc module
    '''
    try:
      from rpncalc import ReversePolishNotationExpression
    except ImportError:
      self.fail('Could not import calculator')

  def test_shell(self):
    '''
    Tests that the module can be called from the shell
    '''
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(['python', 'rpncalc.py', '4 2 /'], stdout=subprocess.PIPE)
      response = command.communicate()[0].decode()
      self.assertEqual(Decimal('2'), Decimal(response))
    else:
      self.fail('rpncalc.py not found.')

  def test_shell_err1(self):
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(['python', 'rpncalc.py', '1 +'], stderr=subprocess.PIPE)
      response = command.communicate()[1]
      self.assertIn('not enough operands', response.decode())
    else:
      self.fail('rpncalc.py not found.')

  def test_shell_err2(self):
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(['python', 'rpncalc.py', 'a b +'], stderr=subprocess.PIPE)
      response = command.communicate()[1]
      self.assertIn('numbers and operators', response.decode())
    else:
      self.fail('rpncalc.py not found.')


def test_generator(expression, value):
  '''
  Generates additional test cases for a particular expression and value, used below.
  '''
  def test(self):
    from rpncalc import ReversePolishNotationExpression
    rpnExpression = ReversePolishNotationExpression(expression)
    self.assertEqual(rpnExpression.calculate(), Decimal(value))
  return test


if __name__ == '__main__':
  # generate test cases for each expression in TEST_EXPRESSIONS before running tests
  for expression in TEST_EXPRESSIONS:
    test_name = '_'.join(['test', expression[0]])
    test = test_generator(expression[1], expression[2])
    setattr(RpnTest, test_name, test)
  unittest.main()
