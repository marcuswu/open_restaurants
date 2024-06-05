import unittest
from dataclasses import dataclass
from weekday import Weekday

class TestWeekday(unittest.TestCase):
    def test_of(self):
        @dataclass
        class TestCase:
            name: str
            input: str 
            expected: Weekday
        
        testcases = [
            TestCase(
                name="m",
                input="m",
                expected=Weekday.MONDAY
            ),
            TestCase(
                name="mon",
                input="mon",
                expected=Weekday.MONDAY
            ),
            TestCase(
                name="Monday",
                input="Monday",
                expected=Weekday.MONDAY
            ),
            TestCase(
                name="t",
                input="t",
                expected=Weekday.TUESDAY
            ),
            TestCase(
                name="Tue",
                input="Tue",
                expected=Weekday.TUESDAY
            ),
            TestCase(
                name="Tuesday",
                input="Tuesday",
                expected=Weekday.TUESDAY
            ),
            TestCase(
                name="w",
                input="w",
                expected=Weekday.WEDNESDAY
            ),
            TestCase(
                name="w",
                input="w",
                expected=Weekday.WEDNESDAY
            ),
            TestCase(
                name="w",
                input="w",
                expected=Weekday.WEDNESDAY
            ),
            TestCase(
                name="Wed",
                input="Wed",
                expected=Weekday.WEDNESDAY
            ),
            TestCase(
                name="Wed",
                input="Wednesday",
                expected=Weekday.WEDNESDAY
            ),
            TestCase(
                name="Th",
                input="Th",
                expected=Weekday.THURSDAY
            ),
            TestCase(
                name="Thu",
                input="Thu",
                expected=Weekday.THURSDAY
            ),
            TestCase(
                name="Thur",
                input="Thur",
                expected=Weekday.THURSDAY
            ),
            TestCase(
                name="Thursday",
                input="Thursday",
                expected=Weekday.THURSDAY
            ),
            TestCase(
                name="F",
                input="F",
                expected=Weekday.FRIDAY
            ),
            TestCase(
                name="Fr",
                input="Fr",
                expected=Weekday.FRIDAY
            ),
            TestCase(
                name="Fri",
                input="Fri",
                expected=Weekday.FRIDAY
            ),
            TestCase(
                name="Friday",
                input="Friday",
                expected=Weekday.FRIDAY
            ),
            TestCase(
                name="Sa",
                input="Sa",
                expected=Weekday.SATURDAY
            ),
            TestCase(
                name="Sat",
                input="Sat",
                expected=Weekday.SATURDAY
            ),
            TestCase(
                name="Saturday",
                input="Saturday",
                expected=Weekday.SATURDAY
            ),
            TestCase(
                name="Su",
                input="Su",
                expected=Weekday.SUNDAY
            ),
            TestCase(
                name="Sun",
                input="Sun",
                expected=Weekday.SUNDAY
            ),
            TestCase(
                name="Sunday",
                input="Sunday",
                expected=Weekday.SUNDAY
            ),
        ]

        for case in testcases:
            actual = Weekday.of(case.input)
            self.assertEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected,
                    actual
                )
            )