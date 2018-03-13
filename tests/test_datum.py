""" Test Datum functions """
from pydatum import Datum


def test_instantiation():
    """ Test creation of the object """
    actual = Datum()
    assert actual is not None

def test_init_value():
    """ The initial value should be now """
    from datetime import datetime

    datum = Datum()
    now = datetime.now()
    assert now == datum.value
