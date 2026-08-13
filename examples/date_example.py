"""Examples demonstrating the date utilities."""

from datetime import date

from pyutils.date_utils import (
    add_days,
    days_between_dates,
    format_date,
    is_weekend,
)


def main() -> None:
    """Run examples for all date utility functions."""

    start = date(2026, 8, 10)
    end = date(2026, 8, 15)

    print("Days between dates:")
    print(f"days_between_dates({start}, {end}) -> "
          f"{days_between_dates(start, end)}")

    print("\nAdd days:")
    print(f"add_days({start}, 5) -> {add_days(start, 5)}")
    print(f"add_days({start}, -3) -> {add_days(start, -3)}")

    print("\nWeekend detection:")
    saturday = date(2026, 8, 8)
    monday = date(2026, 8, 10)

    print(f"is_weekend({saturday}) -> {is_weekend(saturday)}")
    print(f"is_weekend({monday}) -> {is_weekend(monday)}")

    print("\nDate formatting:")
    print(f"format_date({start}) -> {format_date(start)}")
    print(f"format_date({date(2026, 1, 5)}) -> "
          f"{format_date(date(2026, 1, 5))}")


if __name__ == "__main__":
    main()