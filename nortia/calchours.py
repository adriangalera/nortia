from datetime import timedelta
from nortia.date_format import from_str


def calc_hours(row):
    day_acc_hours = __calc_intra_day_acc_hours__(row)
    if day_acc_hours:
        row.extend(to_hours_minutes_seconds(day_acc_hours))
    return row


def calc_accumulated_hours(rows, working_hours_per_day=8):
    acc_hours = None
    complete_days = 0
    for row in rows:
        day_td = __calc_intra_day_acc_hours__(row)
        if day_td:
            complete_days += 1
            if acc_hours is None:
                acc_hours = day_td
            else:
                acc_hours = acc_hours + day_td
    expected_hours = working_hours_per_day * complete_days
    acc_hours = acc_hours - timedelta(hours=expected_hours)
    return to_hours_minutes_seconds(acc_hours)


def __calc_intra_day_acc_hours__(row):
    start_dt = None
    acc_hours = None
    for time in row:
        if "IN" in time:
            time = time.replace("IN:", "")
            start_dt = from_str(time)
        else:
            time = time.replace("OUT:", "")
            end_dt = from_str(time)

            time_difference = end_dt - start_dt
            if acc_hours is None:
                acc_hours = time_difference
            else:
                acc_hours = acc_hours + time_difference
    return acc_hours


def to_hours_minutes_seconds(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return [str(hours), str(minutes), str(seconds)]
