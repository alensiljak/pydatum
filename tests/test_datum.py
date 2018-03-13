""" Test Datum functions """
from pydatum import Datum
from datetime import datetime

def test_instantiation():
    """ Test creation of the object """
    actual = Datum()
    assert actual is not None

def test_init_value():
    """ The initial value should be now """
    datum = Datum()
    now = datetime.now()
    assert now == datum.value

def test_add_days():
    datum = Datum()
    datum.today()
    datum.start_of_day()

    # TODO this will fail at the end of the month!
    today = datetime.today()
    day = today.day + 1
    tomorrow = today.replace(day=day, hour=0, minute=0, second=0, microsecond=0)
    
    actual = datum.add_days(1)
    
    assert actual == tomorrow

def test_start_of_day():
    datum = Datum()
    datum.start_of_day()
    actual = datum.value

    assert actual.hour == 0
    assert actual.minute == 0
    assert actual.second == 0
