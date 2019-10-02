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
