from datetime import datetime
import csv
import re

from nortia.date_format import today, now


def write_now_in(file,  time_fn=datetime.now):
    __write_entry__("IN", file, time_fn())


def write_now_out(file, time_fn=datetime.now):
    __write_entry__("OUT", file, time_fn())


def __write_entry__(keyword, file, time):
    today_str = today(time)
    entries = read_all(file=file)
    now_str = now(time)
    new_entry = f"{keyword}:{now_str}"
    entries_for_today = entries.get(today_str, [])
    entries_for_today.append(new_entry)
    entries[today_str] = entries_for_today
    __save_csv__(entries, file)


def read_today(file, time_fn=datetime.now):
    entries = read_all(file=file)
    today_str = today(time_fn())
    return entries.get(today_str, None)


def read_all(file):
    entries = {}
    with open(file, 'r', encoding='utf-8') as csvfile:
        timesreader = csv.reader(csvfile)
        for row in timesreader:
            day = row[0]
            entries_for_day = row[1:]
            entries[day] = entries_for_day
    return entries


def replace(file, search_term, replace_term):
    regex = r"(IN|OUT):([0-9]{4})-([0-9]{2}-([0-9]{2})) ([0-9]{2}):([0-9]{2}):([0-9]{2})"
    regex = re.compile(regex)
    match_search = regex.match(search_term)
    match_replace = regex.match(replace_term)
    if match_search is None or match_replace is None:
        raise ValueError(f"Could not replace {search_term} for {replace_term}")

    with open(file, 'r', encoding='utf-8') as fd:
        filedata = fd.read()

    filedata = filedata.replace(search_term, replace_term)

    with open(file, 'w', encoding='utf-8') as fd:
        fd.write(filedata)

    return read_all(file)


def __save_csv__(entries, file):
    with open(file, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for day, day_entries in entries.items():
            row = [day]
            row.extend(day_entries)
            writer.writerow(row)
