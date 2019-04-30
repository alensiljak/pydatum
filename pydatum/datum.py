"""
Datetime utilities similar to Joda Time or Calendar in Java 
See https://pymotw.com/2/datetime/ for more arithmetic.
"""
import calendar
from datetime import date, datetime, time, timedelta
#from logging import DEBUG, log

from dateutil.relativedelta import relativedelta

ISO_DATE_FORMAT = "%Y-%m-%d"
ISO_LONG_FORMAT = "%Y-%m-%dT%H:%M:%S"
ISO_FULL_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class Datum:
    """ Encapsulates datetime value and provides operations on top of it """

    def __init__(self):
        self.value: datetime = datetime.now()

    @staticmethod
    def parse(value: str):
        """ Parse date string. Currently only ISO strings supported yyyy-mm-dd. """
        result = Datum()

        result.from_iso_date_string(value)

        return result

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
        copy = Datum()
        copy.from_datetime(self.value)
        return copy

    @property
    def date(self) -> date:
        """ Returns the date value """
        return self.value.date()

    @property
    def time(self) -> time:
        """ The time value """
        return self.value.time()

    @property
    def datetime(self) -> datetime:
        ''' The datetime value. '''
        return self.value

    def from_date(self, value: date) -> datetime:
        """ Initializes from the given date value """
        assert isinstance(value, date)

        #self.value = datetime.combine(value, time.min)
        self.value = datetime(value.year, value.month, value.day)
        return self.value

    def from_datetime(self, value: datetime) -> datetime:
        assert isinstance(value, datetime)

        self.value = value
        return self.value

    def from_iso_long_date(self, date_str: str) -> datetime:
        """ Parse ISO date string (YYYY-MM-DDTHH:mm:ss) """
        assert isinstance(date_str, str)
        assert len(date_str) == 19

        self.value = datetime.strptime(date_str, ISO_LONG_FORMAT)
        return self.value

    def from_iso_date_string(self, date_str: str) -> datetime:
        """ Parse ISO date string (YYYY-MM-DD) """
        assert isinstance(date_str, str)

        self.value = datetime.strptime(date_str, ISO_DATE_FORMAT)
        return self.value

    def get_day(self) -> int:
        """ Returns the day value """
        return self.value.day

    def get_day_name(self) -> str:
        """ Returns the day name """
        weekday = self.value.isoweekday() - 1
        return calendar.day_name[weekday]

    def get_iso_date_string(self):
        return self.to_iso_date_string()

    def to_iso_date_string(self):
        """ Gets the iso string representation of the given date """
        return self.value.strftime(ISO_DATE_FORMAT)

    def get_iso_string(self) -> str:
        return self.to_iso_string()

    def to_iso_string(self) -> str:
        """ Returns full ISO string for the given date """
        assert isinstance(self.value, datetime)
        return datetime.isoformat(self.value)

    def get_month(self) -> int:
        """ Returns the year """
        return self.value.month

    def get_year(self) -> int:
        """ Returns the year """
        return self.value.year

    def end_of_day(self) -> datetime:
        """ End of day """
        self.value = datetime(self.value.year, self.value.month, self.value.day, 23, 59, 59)
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

    def is_end_of_month(self) -> bool:
        """ Checks if the date is at the end of the month """
        end_of_month = Datum()
        # get_end_of_month(value)
        end_of_month.end_of_month()
        return self.value == end_of_month.value

    def set_day(self, day: int) -> datetime:
        """ Sets the day value """
        self.value = self.value.replace(day=day)
        return self.value

    def set_value(self, value: datetime):
        """ Sets the current value """
        assert isinstance(value, datetime)

        self.value = value

    def start_of_day(self) -> datetime:
        """ Returns start of day """
        self.value = datetime(self.value.year, self.value.month, self.value.day)
        return self.value

    def subtract_days(self, days: int) -> datetime:
        """ Subtracts dates from the given value """
        self.value = self.value - relativedelta(days=days)
        return self.value

    def subtract_weeks(self, weeks: int) -> datetime:
        """ Subtracts number of weeks from the current value """
        self.value = self.value - timedelta(weeks=weeks)
        return self.value

    def subtract_months(self, months: int) -> datetime:
        """ Subtracts a number of months from the current value """
        self.value = self.value - relativedelta(months=months)
        return self.value

    def to_short_time_string(self) -> str:
        """ Return the iso time string only. i.e. 22:33 """
        hour = self.time.hour
        minute = self.time.minute
        return f"{hour:02}:{minute:02}"

    def to_long_time_string(self) -> str:
        """ Return the iso time string only. i.e. """
        hour = self.time.hour
        minute = self.time.minute
        second = self.time.second
        return f"{hour:02}:{minute:02}:{second:02}"

    # def to_iso_time_string(self) -> str:
    #     """ Return the iso time string only. i.e. 22:33:44 """
    #     short_time = self.to_short_time_string()
    #     second = self.time.second
    #     return f"{short_time}:{second:02}"

    def to_datetime_string(self) -> str:
        """ Returns a human-readable string representation with iso date and time
        Example: 2018-12-06 12:32:56
        """
        date_display = self.to_iso_date_string()
        time_display = self.to_long_time_string()
        return f"{date_display} {time_display}"

    def to_long_datetime_string(self) -> str:
        """ Returns the long date/time string
        Example: 2018-12-06 12:34
        """
        date_display = self.to_iso_date_string()
        time_display = self.to_short_time_string()
        return f"{date_display} {time_display}"


    def today(self) -> datetime:
        """ Returns today (date only) as datetime """
        self.value = datetime.combine(datetime.today().date(), time.min)
        return self.value

    def yesterday(self) -> datetime:
        """ Set the value to yesterday """
        self.value = datetime.today() - timedelta(days=1)
        return self.value

    def __repr__(self):
        """ string representation """
        #iso_str = self.to_iso_string()
        datetime_str = self.to_datetime_string()

        return f"{datetime_str}"
