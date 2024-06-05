import unittest
import datetime
from dataclasses import dataclass
from restaurant_day import RestaurantDay

class TestRestaurantDay(unittest.TestCase):
    def test_construction(self):
        @dataclass
        class TestCase:
            name: str
            restaurant_day: RestaurantDay
            expected_name: str
            expected_min_hour: int
            expected_min_minute: int
            expected_max_hour: int
            expected_max_minute: int
        
        testcases = [
            TestCase(
                name="simple",
                restaurant_day=RestaurantDay(name="simple", hours="9 am - 10 pm"),
                expected_name="simple",
                expected_min_hour=9,
                expected_min_minute=0,
                expected_max_hour=22,
                expected_max_minute=0
            ),
            TestCase(
                name="max hour in next day",
                restaurant_day=RestaurantDay(name="simple", hours="9 am - 2 am"),
                expected_name="simple",
                expected_min_hour=9,
                expected_min_minute=0,
                expected_max_hour=26,
                expected_max_minute=0
            ),
            TestCase(
                name="min with minutes",
                restaurant_day=RestaurantDay(name="simple2", hours="9:20 am - 10 pm"),
                expected_name="simple2",
                expected_min_hour=9,
                expected_min_minute=20,
                expected_max_hour=22,
                expected_max_minute=0
            ),
            TestCase(
                name="max with minutes",
                restaurant_day=RestaurantDay(name="simple2", hours="9:20 am - 10:30 pm"),
                expected_name="simple2",
                expected_min_hour=9,
                expected_min_minute=20,
                expected_max_hour=22,
                expected_max_minute=30
            ),
            TestCase(
                name="no spacing",
                restaurant_day=RestaurantDay(name="no spacing", hours="9pm-10:30pm"),
                expected_name="no spacing",
                expected_min_hour=21,
                expected_min_minute=0,
                expected_max_hour=22,
                expected_max_minute=30
            ),
            TestCase(
                name="24 hr clock",
                restaurant_day=RestaurantDay(name="24 hr", hours="9:20 - 22:30"),
                expected_name="24 hr",
                expected_min_hour=9,
                expected_min_minute=20,
                expected_max_hour=22,
                expected_max_minute=30
            ),
            TestCase(
                name="24 hr clock no spacing",
                restaurant_day=RestaurantDay(name="24 hr no spacing", hours="9-22:30"),
                expected_name="24 hr no spacing",
                expected_min_hour=9,
                expected_min_minute=0,
                expected_max_hour=22,
                expected_max_minute=30
            ),
        ]

        for case in testcases:
            self.assertEqual(
                case.expected_name,
                case.restaurant_day.name,
                "failed test {} name expected {}, actual {}".format(
                    case.name,
                    case.expected_name,
                    case.restaurant_day.name
                )
            )
            self.assertEqual(
                case.expected_min_hour,
                case.restaurant_day.min_hour,
                "failed test {} min_hour expected {}, actual {}".format(
                    case.name,
                    case.expected_min_hour,
                    case.restaurant_day.min_hour
                )
            )
            self.assertEqual(
                case.expected_min_minute,
                case.restaurant_day.min_minute,
                "failed test {} min_minute expected {}, actual {}".format(
                    case.name,
                    case.expected_min_minute,
                    case.restaurant_day.min_minute
                )
            )
            self.assertEqual(
                case.expected_max_hour,
                case.restaurant_day.max_hour,
                "failed test {} max_hour expected {}, actual {}".format(
                    case.name,
                    case.expected_max_hour,
                    case.restaurant_day.max_hour
                )
            )
            self.assertEqual(
                case.expected_max_minute,
                case.restaurant_day.max_minute,
                "failed test {} max_minute expected {}, actual {}".format(
                    case.name,
                    case.expected_max_minute,
                    case.restaurant_day.max_minute
                )
            )

    def test_contains(self):
        restaurant_day = RestaurantDay(name="simple", hours="9 am - 10 pm")
        @dataclass
        class TestCase:
            name: str
            input: datetime.time
            expected: bool 
        
        testcases = [
            TestCase(
                name="way past",
                input=datetime.datetime.fromisoformat("2024-06-04T23:37:23.988414"),
                expected=False
            ),
            TestCase(
                name="minute past",
                input=datetime.datetime.fromisoformat("2024-06-04T22:01:00.000"),
                expected=False
            ),
            TestCase(
                name="second past",
                input=datetime.datetime.fromisoformat("2024-06-04T22:00:01.000"),
                expected=False
            ),
            TestCase(
                name="millisecond past",
                input=datetime.datetime.fromisoformat("2024-06-04T22:00:00.001"),
                expected=False
            ),
            TestCase(
                name="millisecond past",
                input=datetime.datetime.fromisoformat("2024-06-04T12:00:00.001"),
                expected=True
            ),
        ]

        for case in testcases:
            actual = restaurant_day.contains(case.input)
            self.assertEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected,
                    actual
                )
            )

