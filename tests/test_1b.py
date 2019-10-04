import unittest
from week00_python_basic.challenge_1b.run_1b import find_max_claim
import textwrap
import filecmp

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            invalid_input = '/any/path/not/exist'
            find_max_claim(input=invalid_input, output='any/thing')
        assert str(ec.exception) == f'File {invalid_input} not found'

    def test_tc01(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.c94ptzuqqtop
        valid_input = '/tmp/tc01.input'
        lines = textwrap.dedent('''
            0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion

        # region make expected output
        actual_output = '/tmp.tc01.out'
        expected_output = '/tmp/tc01.expected.out'
        open(expected_output, 'w').close()
        #endregion

        # run testes code
        find_max_claim(valid_input, actual_output)

        # check for expected values
        filecmp.cmp(actual_output, expected_output)

    def test_tc02(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.w2a1103zyh53
        valid_input = '/tmp/tc02.input'
        lines = textwrap.dedent('''
            4
            0
            -22
            3
            44
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion

        #region make expected output
        actual_output = '/tmp/tc02.out'
        expected_output = '/tmp/tc02.expected.out'
        lines_eo = textwrap.dedent('''
            0
            0
            0
            1
        ''').strip()
        with open(expected_output, 'w') as feo:
            print(lines_eo, file=feo)
        #endregion

        # run testes code
        find_max_claim(valid_input, actual_output)

        # check for expected values
        filecmp.cmp(actual_output, expected_output)

    def test_tc03a(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.e3cieiz84v1i
        valid_input = '/tmp/tc03a.input'
        lines = textwrap.dedent('''
            abc
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc03a.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'N must be an integer number'

    def test_tc03b(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.v5dmpp98umnc
        valid_input = '/tmp/tc03b.input'
        with open(valid_input, 'w') as f:
            print('', file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc03b.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'N must have a value'

    def test_tc03c(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.rjt0hzegdweo
        valid_input = '/tmp/tc03c.input'
        open(valid_input, 'w').close()
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc03c.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'Invalid input: Empty file'

    def test_tc04a(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.jfgz7yrat44n
        valid_input = '/tmp/tc04a.input'
        lines = textwrap.dedent('''
            4
            0
            1
            abc
            2
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc04a.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'Invalid input: All claim count must be a number'

    def test_tc04b(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.bfnsn71ffq4t
        valid_input = '/tmp/tc04b.input'
        lines = textwrap.dedent('''
            4
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc04b.out'
            find_max_claim(valid_input, actual_output)
        assert str(ec.exception) == f'All claim-count must be valid'

