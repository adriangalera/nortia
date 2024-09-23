import unittest
from nortia.calchours import calc_hours


class TestHourCalculations(unittest.TestCase):
    def test_normal_day(self):
        row = [
            "IN:2024-09-23 08:00:00",
            "OUT:2024-09-23 10:00:00",
            "IN:2024-09-23 12:00:00",
            "OUT:2024-09-23 14:00:00"
        ]

        new_row = calc_hours(row)
        expected_hours = 4
        expected_minutes = 0
        expected_seconds = 0

        self.assertEqual(expected_seconds, new_row[-1])
        self.assertEqual(expected_minutes, new_row[-2])
        self.assertEqual(expected_hours, new_row[-3])

    def test_not_marked_at_lunch(self):
        row = [
            "IN:2024-09-23 09:00:00",
            "OUT:2024-09-23 19:00:00"
        ]

        new_row = calc_hours(row)
        expected_hours = 10
        expected_minutes = 0
        expected_seconds = 0

        self.assertEqual(expected_seconds, new_row[-1])
        self.assertEqual(expected_minutes, new_row[-2])
        self.assertEqual(expected_hours, new_row[-3])
