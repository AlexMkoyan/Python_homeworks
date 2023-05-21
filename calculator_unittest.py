import unittest
import sys
from calculator import calculator


class CalculatorTest(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('5-3'), 2)

    def test_multiply(self):
        self.assertEqual(calculator('23*4'), 92)

    def test_divde(self):
        self.assertEqual(calculator('9/3'), 3)

    def test_true(self):
        self.assertTrue(calculator('5+5'))

    def test_false(self):
        self.assertFalse(calculator('5-5'))

    def test_is(self):
        self.assertIs(calculator('12+15'), 27)

    def test_isnot(self):
        self.assertIsNot(calculator('12+12'), 23)

    def test_is_not_none(self):
        self.assertIsNotNone(calculator('1-100'))

    def test_in(self):
        self.assertIn(calculator('15+15'), [12, 13, 15, 30])

    def test_notin(self):
        self.assertNotIn(calculator('5+2'), [1, 2, 3])

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('asdf')
        self.assertEqual('The expression must contain at least one sign (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('5+3+9')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('6+8*2')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('6.6+3.5')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('6+8a')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_zerodivision(self):
        with self.assertRaises(ZeroDivisionError) as e:
            calculator('5/0')
        self.assertEqual('Division by zero is not allowed', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()


# Create a test suite
suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)

# Save the verbose output to a file using shell redirection
with open('Unittest_results.txt', 'w') as f:
    # Run the tests with verbosity and redirect the output to the file
    unittest.TextTestRunner(stream=f, verbosity=2).run(suite)

