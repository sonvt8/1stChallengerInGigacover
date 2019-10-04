import unittest

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


def f_no_exception():
    pass

EXCEPTION_MSG = f'some error from f_with_exception'
def f_with_exception():
    raise Exception(EXCEPTION_MSG)


class Test(unittest.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    def test00(self):
        self.fail('Fail on purpose')
        self.fail('We SHOULD NOT reach here')


    def test01_f_no_exception(self):
        try:
            f_no_exception()
            print('We SHOULD reach here as no exception from calling f_no_exception()')
        except Exception as e:
            self.fail('We SHOULD NOT reach here')


    #region f_with_exception()

    def test02_f_with_exception(self):
        try:
            f_with_exception()
            NOT_HERE = 'We SHOULD NOT reach here'; self.fail(NOT_HERE)  # this fail() also raise exception ie AssertError --> we have below line to check: assert str(e) != NOT_HERE - should use a better way to assert exception as test02b_f_with_exception()
        except Exception as e:
            assert str(e) != NOT_HERE, NOT_HERE
            print('We SHOULD reach here as exception has already been raised by f_with_exception()')

    def test02b_f_with_exception(self):
        with self.assertRaises(Exception):
            f_with_exception()

    def test02b_f_with_exception_WILL_FAIL(self):
        with self.assertRaises(Exception):
            f_no_exception()

    def test02b_f_with_exception_TEST_EXCEPTION_MSG(self):
        with self.assertRaises(Exception) as ec:  # ec aka. exception context
            f_with_exception()
        assert str(ec.exception) == EXCEPTION_MSG
    #endregion f_with_exception()
