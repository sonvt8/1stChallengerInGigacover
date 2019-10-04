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
        actual_output = '/tmp/tc00.out'
        expected_output = '/tmp/tc01.expected.out'
        with open(expected_output, 'w') as fo:
            print('', file=fo)

        # run testes code
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc01_tc02(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.4g8u3yvsoc7f
        valid_input = '/tmp/tc01_tc02.input'
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
        actual_output = '/tmp/tc01_tc02.out'
        expected_output = '/tmp/tc01_tc02.expected.out'
        lines_out = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            S122333aG, An V. NGUYEN, 39, 1500
            S122333bG, Binh T. TRAN, 29, 500
        ''').strip()
        with open(expected_output, 'w') as fo:
            print(lines_out, file=fo)

        # run testes code
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc03_tc04(self):
        #region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.7r8ck1i20run
        valid_input = '/tmp/tc03_tc04.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            2
            S122333aG thuOnG bInh vU 1999-01-22 500 2   
            S122333bG triNH Do CAo 2000-02-11 500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        # egion make expected output
        actual_output = '/tmp/tc03_tc04.out'
        expected_output = '/tmp/tc03_tc04.expected.out'
        lines_out = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            S122333aG, Thuong B. VU, 20, 1500
            S122333bG, Trinh D. CAO, 19, 1000
        ''').strip()
        with open(expected_output, 'w') as fo:
            print(lines_out, file=fo)

        # run testes code
        insurance_policies(valid_input, actual_output)

        # check for expected values
        assert filecmp.cmp(actual_output, expected_output)

    def test_tc05a(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.vn2rpimh9xvp
        valid_input = '/tmp/tc05a.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            1 an van nguyen 1999-01-22 500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc05a.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'n must be a string'

    def test_tc05b(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.4or02ub25guj
        valid_input = '/tmp/tc05b.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            empty an van nguyen 1999-01-22 500 0
        ''').strip().replace("empty", '')
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc05b.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'n must have a value'

    def test_tc06a(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.avsqnj1qeba3
        valid_input = '/tmp/tc06a.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG 0 0 0 1990-02-11 500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc06a.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must be a string'

    def test_tc06b(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.y618786kmtie
        valid_input = '/tmp/tc06b.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG ab1cd ab1cd ab1cd 1990-02-11 500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc06b.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must not include number'

    def test_tc06c(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.djcmn0dlr5f3
        valid_input = '/tmp/tc06c.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG empty empty empty 1990-02-11 500 0
        ''').strip().replace('empty', '')
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc06c.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f's must have a value'

    def test_tc07a(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.aptazpl02c30
        valid_input = '/tmp/tc07a.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG trinh do cao abcd-12-34 500 2
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc07a.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'd must be a date i.e. yyyy-mm-dd'

    def test_tc07b(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.z8vx14fyvskh
        valid_input = '/tmp/tc07b.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG thuong binh vu empty 1
        ''').strip().replace('empty', '')
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc07b.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'd must have a value'

    def test_tc08a(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.79gt5un0wtc2
        valid_input = '/tmp/tc08a.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG binh thi tran 1990-02-11 -500 0
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc08a.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'p must be a positive float number'

    def test_tc08b(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.d5q872q8kj3l
        valid_input = '/tmp/tc08b.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG binh thi tran 1990-02-11 empty 0
        ''').strip().replace('empty', '')
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc08b.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'p must have a value'

    def test_tc09a(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.8gw4r2c1oftj
        valid_input = '/tmp/tc09a.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG trinh do cao 2000-02-11 500 abc
        ''').strip()
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc09a.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'c must be a not-negative integer'

    def test_tc09b(self):
        # region make input file as https://docs.google.com/document/d/1v1FcxCLvVGZcAIKy1Q6aPCq3bevR64igyLG4O60JptE/edit#bookmark=id.g2o57ezfn79p
        valid_input = '/tmp/tc09b.input'
        lines = textwrap.dedent('''
            nricfin first_name middle_name last_name date_of_birth premium claim_count
            1
            S122333bG trinh do cao 2000-02-11 500 empty
        ''').strip().replace('empty', '')
        with open(valid_input, 'w') as f:
            print(lines, file=f)
        # endregion

        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            actual_output = '/tmp/tc09b.out'
            insurance_policies(valid_input, actual_output)
        assert str(ec.exception) == f'c must have a value'

