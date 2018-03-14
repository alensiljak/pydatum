""" Test Datum functions """
from pydatum import Datum
from datetime import datetime
from dateutil.relativedelta import relativedelta

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

    today = datetime.today()
    #day = today.day + 1
    tomorrow = today + relativedelta(days=1)
    tomorrow = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    
    actual = datum.add_days(1)
    
    assert actual == tomorrow

def test_start_of_day():
    datum = Datum()
    datum.start_of_day()
    actual = datum.value

    assert actual.hour == 0
    assert actual.minute == 0
    assert actual.second == 0

def test_clone():
    one = Datum()
    two = one.clone()

    assert one.value == two.value

def test_from_iso_date_string():
    str_value = "2017-08-23"
    datum = Datum()
    datum.from_iso_date_string(str_value)

    assert datum.value.day == 23
    assert datum.value.month == 8
    assert datum.value.year == 2017
