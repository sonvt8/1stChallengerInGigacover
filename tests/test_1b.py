import unittest
from week00_python_basic.challenge_1b.testRun import is_max_claim_count
import textwrap
import filecmp

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.c94ptzuqqtop
        valid_input = '/tmp/tc00.input'
        lines = textwrap.dedent('''
            0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        #endregion
        try:
            actual_output = '/any/thing/'
            is_max_claim_count(valid_input, actual_output)
            self.fail('We must NOT reach here')
        except Exception as e:
            pass  # must get here
            assert str(e) == f'List of claim count is empty'

    def test_tc01(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.w2a1103zyh53
        valid_input = '/tmp/tc01.input'
        lines =textwrap.dedent('''
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
        actual_output = '/tmp/tc01.out'
        expected_output = '/tmp/tc01.expected.out'
        lines_eo = textwrap.dedent('''
            0
            0
            0
            1
        ''').strip()
        with open(valid_input, 'w') as feo:
            print(lines_eo, file=feo)
        #endregion

        # run testes code
        is_max_claim_count(valid_input, actual_output)

        # check for expected values
        filecmp.cmp(actual_output, expected_output)
