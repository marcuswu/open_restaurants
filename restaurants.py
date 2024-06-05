import csv
from datetime import time
from restaurant_day import RestaurantDay
from weekday import Weekday
from utils import split_hours, days_for_range

class Restaurants:
    dow = {}
    def __init__(self, restaurant_data) -> None:
        csv_file = open(restaurant_data)
        csv_reader = csv.reader(csv_file)
        read_columns = False
        for row in csv_reader:
            if not read_columns:
                read_columns = True
                continue
            print(row)
            restaurant_name = row[0]
            # Parse DoW, hours tuples
            hours = split_hours(row[1])
            # for each tuple, store a RestaurantDay in dow
            for days_range, hours_range in hours:
                for day in days_for_range(days_range):
                    if self.dow.get(day) == None:
                        self.dow[day] = []
                    self.dow[day].append(RestaurantDay(restaurant_name, hours_range))
    
    def open_at(self, day_of_week, check_time:time) -> list[str]:
        print("passed day of week: ", Weekday(day_of_week))
        restaurants = self.dow[Weekday(day_of_week)]
        return list(map(lambda rest: rest.name ,list(filter(lambda rest: rest.contains(check_time), restaurants))))
