import unittest
from dataclasses import dataclass
from weekday import Weekday
import utils

class TestUtils(unittest.TestCase):
    def test_days_for_range(self):
        @dataclass
        class TestCase:
            name: str
            range: str 
            expected: list[Weekday]
        
        testcases = [
            TestCase(
                name="tue",
                range="Tue",
                expected=[Weekday.TUESDAY]
            ),
            TestCase(
                name="wed-fri",
                range="Wed-Fri",
                expected=[Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY]
            ),
            TestCase(
                name="wed - fri",
                range="Wed - Fri",
                expected=[Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY]
            ),
        ]

