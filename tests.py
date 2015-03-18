from decimal import Decimal
import os
import subprocess
import unittest


TEST_EXPRESSIONS = [
    ('igg_expr_one', '1 2 +', '3'),
    ('igg_expr_two', '4 2 /', '2'),
    ('igg_expr_three', '2 3 4 + *', '14'),
    ('igg_expr_four', '3 4 + 5 6 + *', '77'),
    ('igg_expr_five', '13 4 -', '9'),
]


class RpnTest(unittest.TestCase):

  def test_can_import_rpncalc(self):
    '''
    Tests that we can import the calculator function from the rpncalc module.
    '''
    try:
      from rpncalc import calculator
    except ImportError:
      self.fail('Could not import calculator')

  def test_command(self):
    '''
    Tests that the module can be called from the shell
    '''
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(['python', 'rpncalc.py', '4 2 /'], stdout=subprocess.PIPE)
      response = command.communicate()[0].decode()
      self.assertEqual(Decimal('2'), Decimal(response))
    else:
      self.fail('rpncalc.py not found.')

  def test_command_igg_err1(self):
    '''
    Tests indiegogo error scenario one.
    '''
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(
          ['python', 'rpncalc.py', '1 +'],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE
      )
      response = command.communicate()[1]
      self.assertIn('not enough operands', response.decode())
    else:
      self.fail('rpncalc.py not found.')

  def test_command_igg_err2(self):
    '''
    Tests indiegogo error scenario two.
    '''
    if os.path.isfile('rpncalc.py'):
      command = subprocess.Popen(
          ['python', 'rpncalc.py', 'a b +'],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE
      )
      response = command.communicate()[1]
      self.assertIn('numbers and operators', response.decode())
    else:
      self.fail('rpncalc.py not found.')


def test_generator(expression, value):
  '''
  Generates additional test cases for a particular expression and value, used below.
  '''
  def test(self):
    from rpncalc import calculator
    self.assertEqual(calculator(expression), Decimal(value))
  return test


if __name__ == '__main__':
  # generate test cases for each expression in TEST_EXPRESSIONS before running tests
  for expression in TEST_EXPRESSIONS:
    test_name = '_'.join(['test', expression[0]])
    test = test_generator(expression[1], expression[2])
    setattr(RpnTest, test_name, test)
  unittest.main()
