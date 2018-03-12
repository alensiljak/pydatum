""" Datetime utilities similar to Joda Time or Calendar in Java """
import calendar
from datetime import date, datetime, time, timedelta
from logging import DEBUG, log

from dateutil.relativedelta import relativedelta

ISO_SHORT_FORMAT = "%Y-%m-%d"
ISO_LONG_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class Datum:
    """ Encapsulates datetime value and provides operations on top of it """

    def __init__(self, value: datetime = None):
        self.value = datetime() if not value else value

    def add_days(self, days: int) -> datetime:
        """ Adds days """
        self.value = self.value + relativedelta(days=days)
        return self.value

    def add_months(self, value: int) -> datetime:
        """ Add a number of months to the given date """
        self.value = self.value + relativedelta(months=value)
        return self.value

    def clone(self):
        """ Cretes a copy """
        copy = Datum(self.value)
        return copy

    def from_date(self, value: date):
        """ Initializes from the given date value """
        self.value = datetime.combine(value, time.min)

    def get_iso_string(self) -> str:
        """ Returns full ISO string for the given date """
        return datetime.isoformat(self.value)

    def set_value(self, value: datetime):
        """ Sets the current value """
        assert isinstance(value, datetime)

        self.value = value

    def subtract_days(self, days: int) -> datetime:
        """ Subtracts dates from the given value """
        self.value = self.value - relativedelta(days=days)
        return self.value

    def end_of_month(self) -> datetime:
        """ Provides end of the month for the given date """
        # Increase month by 1,
        result = self.value + relativedelta(months=1)
        # take the 1st day of the (next) month,
        result = result.replace(day=1)
        # subtract one day
        result = result - relativedelta(days=1)
        self.value = result
        return self.value

    def today(self) -> datetime:
        """ Returns today (date only) as datetime """
        self.value = datetime.combine(datetime.today().date(), time.min)
        return self.value
