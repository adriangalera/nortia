import unittest
import datetime
import uuid
import os
from nortia.repo import write_now_in, read_today


class TestRepo(unittest.TestCase):

    folder = None
    stubbed_date = datetime.datetime(2019, 1, 1, 0, 0, 0)

    def setUp(self) -> None:
        self.folder = "tests/repo-files/"+str(uuid.uuid4())
        os.system("mkdir -p "+self.folder)
        return super().setUp()

    def test_in(self):
        write_now_in(folder=self.folder, time=self.stubbed_date)
        today_contents = read_today(folder=self.folder, time=self.stubbed_date)
        dt_fmt = self.stubbed_date.strftime("%Y-%m-%d %H:%M:%S")
        expected_contents = f"IN:{dt_fmt}"
        self.assertEqual(expected_contents, today_contents)
