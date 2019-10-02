import unittest
from week00_python_basic.challenge_1a.Test1 import find_min


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now


    def test_tc00(self):
        try:
            invalid_input = '/any/path/not/exist'
            find_min(input=invalid_input, output='any/thing')
        except Exception as e:
            pass  # must get here
            assert str(e) == f'File {invalid_input} not found'

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
