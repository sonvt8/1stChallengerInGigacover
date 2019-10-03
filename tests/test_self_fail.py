import unittest

def f():
    pass


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test_tc00(self):
        try:
            f()
            self.fail('bbbbb')
            return
        except Exception as e:
            pass  # must get here
