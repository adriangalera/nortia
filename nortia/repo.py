from datetime import datetime
import os

REPO_FOLDER = "./storage"

# Keep one file per day


def write_now_in(folder=REPO_FOLDER, time=datetime.now()):
    __write_in_file__("IN", folder, time)


def write_now_out(folder=REPO_FOLDER, time=datetime.now()):
    __write_in_file__("OUT", folder, time)


def read_today(folder=REPO_FOLDER, time=datetime.now()):
    today_file_str = __today_file__(folder, time)
    with open(today_file_str, 'r', encoding='utf-8') as f:
        return f.read()


def read_all():
    pass


def __write_in_file__(keyword, folder, time):
    today_file_str = __today_file__(folder, time)
    cur_time = __now__(time)
    with open(today_file_str, 'r', encoding='utf-8') as f:
        today_content = f.read()
    with open(today_file_str, 'w', encoding='utf-8') as f:
        today_content = today_content + f"{keyword}:{cur_time}"
        f.write(today_content)


def __today__(time):
    return time.strftime("%Y-%m-%d")


def __now__(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")


def __today_file__(folder, time):
    today_str = __today__(time)
    today_file_path = f"{folder}/{today_str}.txt"
    if not os.path.exists(today_file_path):
        os.system(f"touch {folder}")
    return today_file_path
