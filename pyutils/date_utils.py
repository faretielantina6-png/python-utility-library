from datetime import date, timedelta

def days_between_dates(start: date, end: date)-> int:
    """Returns the number of days between two dates."""

    if not isinstance(start, date) or not isinstance(end, date):
        raise TypeError("Both start and end must be datetime.date objects.")
    return abs((end - start).days)

def add_days(date_value: date, days: int)-> date:
    """Returns a new date that is a specified number of days after the given date."""

    if not isinstance(date_value, date):
        raise TypeError("The first argument must be a datetime.date object.")
    if not isinstance(days, int):
        raise TypeError("The second argument must be an integer")
    return date_value + timedelta(days=days)

def is_weekend(date_value: date)-> bool:
    """Returns True if the date falls on Saturday or Sunday."""
    if not isinstance(date_value,date):
        raise TypeError("The dates must be a datetime.date object.")
    return date_value.weekday() >= 5

def format_date(date_value: date)-> str:
    """Returns the date formatted as DD/MM/YYY."""
    if not isinstance(date_value,date):
        raise TypeError("The dates must be a datetime.date object.")
    return date_value.strftime("%d/%m/%Y")