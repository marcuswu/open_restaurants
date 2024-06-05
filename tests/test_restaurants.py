import unittest
import datetime
from typing import Dict
from dataclasses import dataclass
from restaurant_day import RestaurantDay
from restaurants import Restaurants
from weekday import Weekday

class TestRestaurants(unittest.TestCase):
    def test_construction(self):
        @dataclass
        class TestCase:
            name: str
            restaurants: Restaurants
            expected_dow: Dict[Weekday, list[RestaurantDay]]
        
        testcases = [
            TestCase(
                name="simple",
                restaurants=Restaurants([
                    ["Restaurant Name","Hours"],
                    ["The Cowfish Sushi Burger Bar","Mon-Sun 11:00 am - 10 pm"],
                    ["Morgan St Food Hall","Mon-Sun 11 am - 9:30 pm"],
                ]),
                expected_dow={
                    Weekday.MONDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.TUESDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.WEDNESDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.THURSDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.FRIDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.SATURDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                    Weekday.SUNDAY: [
                        RestaurantDay("The Cowfish Sushi Burger Bar", "11:00 am - 10 pm"),
                        RestaurantDay("Morgan St Food Hall","11 am - 9:30 pm"),
                    ],
                }
            ),
        ]

        for case in testcases:
            self.assertDictEqual(
                case.expected_dow,
                case.restaurants.dow,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected_dow,
                    case.restaurants.dow
                )
            )

    def test_open_at(self):
        restaurants = None
        restaurants = Restaurants([
            ["Restaurant Name","Hours"],
            ["The Cowfish Sushi Burger Bar","Mon-Sun 11:00 am - 10 pm"],
            ["Morgan St Food Hall","Mon-Sun 11 am - 9:30 pm"],
        ])
        @dataclass
        class TestCase:
            name: str
            input: datetime.datetime
            expected: list[str] 
        
        testcases = [
            TestCase(
                name="none",
                input=datetime.datetime.fromisoformat("2024-06-04T23:37:23.988414"),
                expected=[]
            ),
            TestCase(
                name="one",
                input=datetime.datetime.fromisoformat("2024-06-04T21:30:23.988414"),
                expected=["The Cowfish Sushi Burger Bar"]
            ),
            TestCase(
                name="both",
                input=datetime.datetime.fromisoformat("2024-06-04T21:20:23.988414"),
                expected=["The Cowfish Sushi Burger Bar", "Morgan St Food Hall"]
            ),
        ]

        for case in testcases:
            actual = restaurants.open_at(day_of_week=case.input.weekday(), check_time=case.input.time())
            self.assertListEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name,
                    case.expected,
                    actual
                )
            )

