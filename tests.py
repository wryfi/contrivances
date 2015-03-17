from decimal import getcontext, Decimal
import unittest

TEST_EXPRESSIONS = [
    ('igg_one', '1 2 +', '3'),
    ('igg_two', '4 2 /', '2'),
    ('igg_three', '2 3 4 + *', '14'),
    ('igg_four', '3 4 + 5 6 + *', '77'),
    ('igg_five', '13 4 -', '9'),
]


class RpnTest(unittest.TestCase):

  def test_can_import_rpncalc(self):
    try:
      from rpncalc import calculator
    except ImportError:
      self.fail('Could not import calculator')


def test_generator(expression, value):
  def test(self):
    from rpncalc import calculator
    print('testing expression %s' % (expression,))
    self.assertEqual(calculator(expression), Decimal(value))
  return test

if __name__ == '__main__':
  for expression in TEST_EXPRESSIONS:
    test_name = '_'.join(['test', expression[0]])
    test = test_generator(expression[1], expression[2])
    setattr(RpnTest, test_name, test)
  unittest.main()
