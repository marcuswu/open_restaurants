import unittest
from dataclasses import dataclass
from weekday import Weekday
import utils

class TestUtils(unittest.TestCase):
    def test_days_for_range(self):
        @dataclass
        class TestCase:
            name: str
            input: str 
            expected: list[Weekday]
        
        testcases = [
            TestCase(
                name="tue",
                input="Tue",
                expected=[Weekday.TUESDAY]
            ),
            TestCase(
                name="junk day",
                input="Blah",
                expected=[]
            ),
            TestCase(
                name="wed-fri",
                input="Wed-Fri",
                expected=[Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY]
            ),
            TestCase(
                name="wed - fri",
                input="Wed - Fri",
                expected=[Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY]
            ),
            TestCase(
                name="looping range",
                input="Fri - Wed",
                expected=[Weekday.FRIDAY, Weekday.SATURDAY, Weekday.SUNDAY, Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY]
            ),
            TestCase(
                name="junk start",
                input="Baz - Fri",
                expected=[]
            ),
            TestCase(
                name="junk end",
                input="Wed - Bar",
                expected=[]
            ),
        ]

        for case in testcases:
            actual = utils.days_for_range(case.input)
            self.assertListEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected,
                    actual
                )
            )


    def test_split_hours(self):
        @dataclass
        class TestCase:
            name: str
            input: str 
            expected: list[tuple[str, str]]
        
        testcases = [
            TestCase(
                name="one tuple",
                input="Mon-Sun 11:00 am - 10 pm",
                expected=[("Mon-Sun", "11:00 am - 10 pm")]
            ),
            TestCase(
                name="one tuple part 2",
                input="Tues-Fri, Sun 11:30 am - 10 pm",
                expected=[("Tues-Fri, Sun", "11:30 am - 10 pm")]
            ),
            TestCase(
                name="two tuples",
                input="Mon-Thu, Sun 11:30 am - 10 pm  / Fri-Sat 11:30 am - 11 pm",
                expected=[("Mon-Thu, Sun", "11:30 am - 10 pm"), ("Fri-Sat", "11:30 am - 11 pm")]
            ),
            TestCase(
                name="four tuples",
                input="Mon-Wed 5 pm - 12:30 am  / Thu-Fri 5 pm - 1:30 am  / Sat 3 pm - 1:30 am  / Sun 3 pm - 11:30 pm",
                expected=[
                    ("Mon-Wed", "5 pm - 12:30 am"),
                    ("Thu-Fri", "5 pm - 1:30 am"),
                    ("Sat", "3 pm - 1:30 am"),
                    ("Sun", "3 pm - 11:30 pm"),
                ]
            ),
        ]

        for case in testcases:
            actual = utils.split_hours(case.input)
            self.assertListEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected,
                    actual
                )
            )