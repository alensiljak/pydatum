""" Date range """
from datetime import datetime


class DateRange:
    """ Represents a date range """
    def __init__(self, start: datetime = None, end: datetime = None):
        self.start: datetime = start
        self.end: datetime = end
