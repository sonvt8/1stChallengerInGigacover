import unittest
from week00_python_basic.challenge_1a.run_1a import find_min


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now


    def test_tc00(self):
        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            invalid_input = '/any/path/not/exist'
            find_min(input=invalid_input, output='any/thing')
        assert str(ec.exception) == f'File {invalid_input} not found'

    def test_tc01(self):
        #region make input file as https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.ej3k2ud0bk6m
        valid_input = '/tmp/tc01.input'
        with open(valid_input, 'w') as f:
            print('1, 22, 333, 44, 55, 66', file=f)
        #endregion

        actual_output = '/tmp/tc01.output'
        find_min(input=valid_input, output=actual_output)
        with open(actual_output, 'r') as fo:
            data = fo.read().strip()
            assert data == '1'

    def test_tc02(self):
        #region make input file as https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.bn49fls8npyl
        valid_input = '/tmp/tc02.input'
        with open(valid_input, 'w') as f:
            print('1, 22, 333', file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/any/thing/'
            find_min(input=valid_input, output=actual_output)
        assert str(ec.exception) == f'Invalid input: List of numbers should have 6 numbers'

    def test_tc03a(self):
        #region make input file as https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.1a6jj95xd435
        valid_input = '/tmp/tc03a.input'
        with open(valid_input, 'w') as f:
            print('1, 22, 333, 44, 555, a', file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc03a.output'
            find_min(input=valid_input, output=actual_output)
        assert str(ec.exception) == f'Invalid input: The item in the list must be a number'

    def test_tc03b(self):
        #region make input file as https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.r0torxrmg9uh
        valid_input = '/tmp/tc03b.input'
        with open(valid_input, 'w') as f:
            print('', file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            find_min(input=valid_input, output='any/thing')
        assert str(ec.exception) == f'Invalid input: List of numbers should have 6 numbers'

    def test_tc03c(self):
        #region make input file as https://docs.google.com/document/d/1spaSZlvmHTDarW6OnKvrKgJKRdbS-mKc/edit#bookmark=id.a6tazu4n6psx
        valid_input = '/tmp/tc03b.input'
        open(valid_input, 'w').close()
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            find_min(input=valid_input, output='any/thing')
        assert str(ec.exception) == f'Invalid input: Empty file'
