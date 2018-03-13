""" Test Datum functions """
from pydatum import Datum


def test_instantiation():
    """ Test creation of the object """
    actual = Datum()
    assert actual is not None
    