#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object self (used in interactive mode)"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return the result"""
        total_seconds = self.to_seconds() + t2.to_seconds()
        total_seconds %= 86400  # Ensure the time wraps around if it exceeds 24 hours
        return self.seconds_to_time(total_seconds)

    def __add__(self, t2):
        """Return the result by using sum_times() method"""
        return self.sum_times(t2)

    def to_seconds(self):
        """Convert the time object to a total number of seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    @staticmethod
    def seconds_to_time(seconds):
        """Convert a given number of seconds to a Time object"""
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time
