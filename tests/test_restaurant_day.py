import unittest
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
                restaurant_day=RestaurantDay(name="no spacing", hours="9am-10:30pm"),
                expected_name="no spacing",
                expected_min_hour=9,
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
