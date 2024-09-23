from datetime import datetime
import csv

REPO_FILE = "./storage/time.csv"


def write_now_in(file=REPO_FILE, time=datetime.now()):
    __write_entry__("IN", file, time)


def write_now_out(file=REPO_FILE, time=datetime.now()):
    __write_entry__("OUT", file, time)


def __write_entry__(keyword, file, time):
    today_str = __today__(time)
    entries = read_all(file=file)
    now_str = __now__(time)
    new_entry = f"{keyword}:{now_str}"
    entries_for_today = entries.get(today_str, [])
    entries_for_today.append(new_entry)
    entries[today_str] = entries_for_today
    __save_csv__(entries, file)


def read_today(file=REPO_FILE, time=datetime.now()):
    entries = read_all(file=file)
    today_str = __today__(time)
    return entries.get(today_str, None)


def read_all(file=REPO_FILE):
    entries = {}
    with open(file, 'r', encoding='utf-8') as csvfile:
        timesreader = csv.reader(csvfile)
        for row in timesreader:
            day = row[0]
            entries_for_day = row[1:]
            entries[day] = entries_for_day
    return entries


def __today__(time):
    return time.strftime("%Y-%m-%d")


def __now__(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")


def __save_csv__(entries, file):
    with open(file, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for day, day_entries in entries.items():
            row = [day]
            row.extend(day_entries)
            writer.writerow(row)
