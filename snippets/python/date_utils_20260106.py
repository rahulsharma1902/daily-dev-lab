"""
Date Utility Functions
"""
from datetime import datetime, timedelta

def days_between(date1, date2):
    """Calculate days between two dates."""
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def add_days(date_str, days):
    """Add days to a date string."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

def is_weekend(date_str):
    """Check if date is weekend."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.weekday() >= 5

def format_date(date_str, from_fmt="%Y-%m-%d", to_fmt="%B %d, %Y"):
    """Convert date format."""
    date = datetime.strptime(date_str, from_fmt)
    return date.strftime(to_fmt)

# Examples
if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Today: {format_date(today)}")
    print(f"Is weekend: {is_weekend(today)}")
