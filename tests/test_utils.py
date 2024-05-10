import unittest
import sys
sys.path.append('../')
from src.utils import bytes_to_gigabytes, kilobytes_per_second_to_megabytes_per_second, milliseconds_to_hours, milliseconds_to_minutes

class TestUnitConversionFunctions(unittest.TestCase):

    def test_bytes_to_gigabytes(self):
        self.assertAlmostEqual(bytes_to_gigabytes(1073741824), 1.0)  # 1 GB in bytes
        self.assertAlmostEqual(bytes_to_gigabytes(5368709120), 5.0)  # 5 GB in bytes

    def test_kilobytes_per_second_to_megabytes_per_second(self):
        self.assertAlmostEqual(kilobytes_per_second_to_megabytes_per_second(1024), 1.0)  # 1 MB/s in KB/s
        self.assertAlmostEqual(kilobytes_per_second_to_megabytes_per_second(5120), 5.0)  # 5 MB/s in KB/s

    def test_milliseconds_to_hours(self):
        self.assertAlmostEqual(milliseconds_to_hours(3600000), 1.0)  # 1 hour in milliseconds
        self.assertAlmostEqual(milliseconds_to_hours(7200000), 2.0)  # 2 hours in milliseconds

    def test_milliseconds_to_minutes(self):
        self.assertAlmostEqual(milliseconds_to_minutes(60000), 1.0)  # 1 minute in milliseconds
        self.assertAlmostEqual(milliseconds_to_minutes(180000), 3.0)  # 3 minutes in milliseconds


if __name__ == '__main__':
    unittest.main()
