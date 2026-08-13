from datetime import date
import pytest

from pyutils.date_utils import(days_between_dates, add_days, is_weekend, format_date)

def test_days_between_dates():
    assert days_between_dates(date(2026, 8,10),date(2026, 8, 15)) == 5

def test_days_between_dates_reverse_order():
    assert days_between_dates(date(2026, 8,15),date(2026, 8, 10)) == 5

def test_days_between_dates_same_date():
    assert days_between_dates(date(2026, 8,10),date(2026, 8, 10)) == 0
    
def test_days_between_dates_invalid_type():
    with pytest.raises(TypeError):
        days_between_dates("2026-08-10",date(2026, 8, 15))  # type: ignore[arg-type]

    
def test_add_days_positive():
    assert add_days(date(2026, 8, 10), 5) == date(2026, 8, 15)

def test_add_zero_days():
    assert add_days(date(2026, 8, 10), 0) == date(2026, 8, 10)

def test_add_days_negative():
    assert add_days(date(2026, 8, 10), -5) == date(2026, 8, 5)

def test_add_days_month_change():
    assert add_days(date(2026, 8, 31), 1) == date(2026, 9, 1)

def test_add_days_year_change():
    assert add_days(date(2026, 12, 31), 1) == date(2027, 1, 1)

def test_add_days_invalid_date():
    with pytest.raises(TypeError):
        add_days("2026-08-10", 5)   # type: ignore[arg-type]

def test_add_days_invalid_days():
    with pytest.raises(TypeError):
        add_days(date(2026, 8, 10), "5")    # type: ignore[arg-type]


def test_is_weekend_saturday():
    assert is_weekend(date(2026, 8, 15)) == True

def test_is_weekend_sunday():
    assert is_weekend(date(2026, 8, 16)) == True

def test_is_weekend_wednesday():
    assert is_weekend(date(2026, 8, 10)) == False

def test_is_weekend_invalid_type():
    with pytest.raises(TypeError):
        is_weekend("2026-08-08") # type: ignore[arg-type]


def test_format_date():
    assert format_date(date(2026, 8, 8)) == "08/08/2026"

def test_format_date_single_digit_day_and_month():
    assert format_date(date(2026, 1, 5)) == "05/01/2026"

def test_format_date_invalid_type():
    with pytest.raises(TypeError):
        format_date("2026-08-08") # type: ignore[arg-type]
