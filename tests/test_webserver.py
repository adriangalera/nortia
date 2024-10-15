import unittest

from nortia.webserver import format_output


class TestWebserver(unittest.TestCase):
    def test_format_date(self):
        entries = {
            "2024-01-01": ["IN:2024-01-01 00:00:00", "OUT:2024-01-01 12:00:00"],
            "2024-01-02": ["IN:2024-01-02 00:00:00", "OUT:2024-01-02 12:00:00"],
        }
        tsv_output = format_output(entries)
        line_one = ["2024-01-01", "IN:2024-01-01 00:00:00",
                    "OUT:2024-01-01 12:00:00", "12", "0", "0"]
        line_two = ["2024-01-02", "IN:2024-01-02 00:00:00",
                    "OUT:2024-01-02 12:00:00", "12", "0", "0"]

        acc_hours_message = "Accumulated hours: 8\t0\t0\n"
        expected_output = acc_hours_message
        expected_output += "\t".join(line_one) + "\n" + "\t".join(line_two) + "\n"

        self.assertEqual(tsv_output, expected_output)
