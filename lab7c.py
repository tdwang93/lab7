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

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from midnight"""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects and return the sum using the new approach"""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    total_seconds %= 86400  # Ensure the time wraps around if it exceeds 24 hours
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify the time object based on the integer value of seconds using the new approach"""
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 86400  # Ensure the time wraps around if it exceeds 24 hours
    if total_seconds < 0:  # Handle negative wrap-around
        total_seconds += 86400
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None
