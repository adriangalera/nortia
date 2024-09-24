import unittest
import datetime
import uuid
import os
from nortia.repo import write_now_in, write_now_out, read_today, read_all


class TestRepo(unittest.TestCase):

    file = None
    stubbed_date = datetime.datetime(2019, 1, 1, 0, 0, 0)
    stubbed_date2 = datetime.datetime(2019, 1, 2, 0, 0, 0)

    def setUp(self) -> None:
        self.file = "tests/repo-files/"+str(uuid.uuid4())+".csv"
        os.system("touch "+self.file)
        return super().setUp()

    def test_in(self):
        def time_fn(): return self.stubbed_date
        write_now_in(file=self.file, time_fn=time_fn)
        today_contents = read_today(file=self.file, time_fn=time_fn)
        dt_fmt = self.stubbed_date.strftime("%Y-%m-%d %H:%M:%S")
        expected_contents = [f"IN:{dt_fmt}"]
        self.assertEqual(expected_contents, today_contents)

    def test_out(self):
        def time_fn(): return self.stubbed_date
        write_now_out(file=self.file, time_fn=time_fn)
        today_contents = read_today(file=self.file, time_fn=time_fn)
        dt_fmt = self.stubbed_date.strftime("%Y-%m-%d %H:%M:%S")
        expected_contents = [f"OUT:{dt_fmt}"]
        self.assertEqual(expected_contents, today_contents)

    def test_multiple_in_out_same_day(self):
        def time_fn(): return self.stubbed_date
        write_now_in(file=self.file, time_fn=time_fn)
        write_now_out(file=self.file, time_fn=time_fn)
        today_contents = read_today(file=self.file, time_fn=time_fn)
        dt_fmt = self.stubbed_date.strftime("%Y-%m-%d %H:%M:%S")
        expected_contents = [f"IN:{dt_fmt}", f"OUT:{dt_fmt}"]
        self.assertEqual(expected_contents, today_contents)

    def test_multiple_days(self):
        def time_fn(): return self.stubbed_date
        def time2_fn(): return self.stubbed_date2

        write_now_in(file=self.file, time_fn=time_fn)
        write_now_out(file=self.file, time_fn=time_fn)
        write_now_in(file=self.file, time_fn=time2_fn)
        write_now_out(file=self.file, time_fn=time2_fn)
        dt_fmt = self.stubbed_date.strftime("%Y-%m-%d %H:%M:%S")
        dt_day_fmt = self.stubbed_date.strftime("%Y-%m-%d")
        dt2_fmt = self.stubbed_date2.strftime("%Y-%m-%d %H:%M:%S")
        dt2_day_fmt = self.stubbed_date2.strftime("%Y-%m-%d")
        expected_contents = {
            dt_day_fmt: [f"IN:{dt_fmt}", f"OUT:{dt_fmt}"],
            dt2_day_fmt: [f"IN:{dt2_fmt}", f"OUT:{dt2_fmt}"],
        }
        all_entries = read_all(file=self.file)
        self.assertEqual(expected_contents, all_entries)
