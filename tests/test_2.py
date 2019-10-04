import unittest
from week00_python_basic.challenge_2.run_2 import insurance_policies
import textwrap
import filecmp

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.q1lpunwc78v8
        valid_input = '/tmp/tc00.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            0    
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        # region make expected output
        actual_output = '/tmp.tc00.out'
        expected_output = '/tmp/tc01.expected.out'
        with open(expected_output, 'w'):
            print('', file=f)

        # run testes code
        insurance_policies(valid_input, actual_output)

        # check for expected values
        filecmp.cmp(actual_output, expected_output)

    def test_tc01_tc02(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.4g8u3yvsoc7f
        valid_input = '/tmp/tc01.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            2
            S122333aG aN vaN nguyeN 1980-02-11 500 2   
            S122333bG binh thi tran 1990-02-11 500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        # region make expected output
        actual_output = '/tmp.tc01.out'
        expected_output = '/tmp/tc01.expected.out'
        lines_out = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            S122333aG, An V. NGUYEN, 39, 1500
            S122333aG, Binh T. TRAN, 29, 500
        ''').strip()
        with open(expected_output, 'w'):
            print(lines_out, file=f)

        # run testes code
        insurance_policies(valid_input, actual_output)

        # check for expected values
        filecmp.cmp(actual_output, expected_output)