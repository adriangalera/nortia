import datetime

DAY_FMT = "%Y-%m-%d"
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"


def today(time):
    return time.strftime(DAY_FMT)


def now(time):
    return time.strftime(DATETIME_FMT)


def from_str(date_str):
    return datetime.datetime.strptime(date_str, DATETIME_FMT)
