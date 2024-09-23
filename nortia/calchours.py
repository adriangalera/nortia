from nortia.date_format import from_str


def calc_hours(row):
    start_dt = None
    timedelta = None
    for time in row:
        if "IN" in time:
            time = time.replace("IN:", "")
            start_dt = from_str(time)
        else:
            time = time.replace("OUT:", "")
            end_dt = from_str(time)

            time_difference = end_dt - start_dt
            if timedelta is None:
                timedelta = time_difference
            else:
                timedelta = timedelta + time_difference

    row.extend(to_hours_minutes_seconds(timedelta))
    return row


def to_hours_minutes_seconds(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return [hours, minutes, seconds]
