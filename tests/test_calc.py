import unittest
from nortia.calchours import calc_hours, calc_accumulated_hours


class TestHourCalculations(unittest.TestCase):
    def test_normal_day(self):
        row = [
            "IN:2024-09-23 08:00:00",
            "OUT:2024-09-23 10:00:00",
            "IN:2024-09-23 12:00:00",
            "OUT:2024-09-23 14:00:00"
        ]

        new_row = calc_hours(row)
        expected_hours = '4'
        expected_minutes = '0'
        expected_seconds = '0'

        self.assertEqual(expected_seconds, new_row[-1])
        self.assertEqual(expected_minutes, new_row[-2])
        self.assertEqual(expected_hours, new_row[-3])

    def test_not_marked_at_lunch(self):
        row = [
            "IN:2024-09-23 09:00:00",
            "OUT:2024-09-23 19:00:00"
        ]

        new_row = calc_hours(row)
        expected_hours = '10'
        expected_minutes = '0'
        expected_seconds = '0'

        self.assertEqual(expected_seconds, new_row[-1])
        self.assertEqual(expected_minutes, new_row[-2])
        self.assertEqual(expected_hours, new_row[-3])

    def test_calculate_hours_accumulated_in_multiple_days(self):
        rows = [
            ["IN:2024-09-23 09:00:00", "OUT:2024-09-23 19:00:00"],  # 10h
            ["IN:2024-09-24 09:00:00", "OUT:2024-09-24 19:00:00"],  # 10h
            # Does not take into account last day (current)
            ["IN:2024-09-25 09:00:00", "OUT:2024-09-26 19:00:00"]
        ]
        acc_hours = calc_accumulated_hours(rows, working_hours_per_day=8)
        expected_hours = '4'
        expected_minutes = '0'
        expected_seconds = '0'

        self.assertEqual(expected_seconds, acc_hours[-1])
        self.assertEqual(expected_minutes, acc_hours[-2])
        self.assertEqual(expected_hours, acc_hours[-3])

    def test_calculate_hours_accumulated_in_multiple_days_not_finished_day(self):
        rows = [
            ["IN:2024-09-23 09:00:00", "OUT:2024-09-23 19:00:00"],  # 10h
            ["IN:2024-09-24 09:00:00", ]   # day not finished
        ]
        acc_hours = calc_accumulated_hours(rows, working_hours_per_day=8)
        expected_hours = '2'
        expected_minutes = '0'
        expected_seconds = '0'

        self.assertEqual(expected_seconds, acc_hours[-1])
        self.assertEqual(expected_minutes, acc_hours[-2])
        self.assertEqual(expected_hours, acc_hours[-3])

    def test_complex_case(self):
        with open('tests/complex.txt', 'r') as complex_example_fd:
            contents = complex_example_fd.readlines()
            rows = []
            for line in contents:
                row = line.replace("\n", "").split("\t")
                rows.append(row)
            acc_hours = calc_accumulated_hours(rows, working_hours_per_day=8)
            self.assertEqual(["4", "37", "43"], acc_hours)
