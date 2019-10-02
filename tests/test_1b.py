import unittest
from week00_python_basic.challenge_1b.testRun import is_max_claim_count
from week00_python_basic.challenge_1b.testRun import writeFile


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        #region make input file as https://docs.google.com/document/d/1SMjeNNPntRFNPrDqngh304hUh9P4cD0L/edit#bookmark=id.c94ptzuqqtop
        valid_input = '/tmp/tc00.input'
        numbers = [0]
        with open(valid_input, 'w') as f:
            for number in numbers:
                print('%i' % number, file=f)
        #endregion
        try:
            actual_output = '/any/thing/'
            is_max_claim_count(valid_input, actual_output)
        except Exception as e:
            pass  # must get here
            assert str(e) == f'List of claim count is empty'




