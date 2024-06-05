import re
from datetime import time

class RestaurantDay:
    name = ""
    min_hour = 0
    max_hour = 24
    min_minute = 0
    max_minute = 0
    def __init__(self, name:str, hours:str) -> None:
        self.name = name
        # todo: parse hours
        time_range = hours.split('-')
        numbers_only = re.compile("^[0-9]+")
        min_time_fields = time_range[0].strip().split(':')
        max_time_fields = time_range[1].strip().split(':')
        self.min_hour = int(numbers_only.findall(min_time_fields[0])[0])
        if len(min_time_fields) > 1:
            self.min_minute = int(numbers_only.findall(min_time_fields[1])[0])
        self.max_hour = int(numbers_only.findall(max_time_fields[0])[0])
        if len(max_time_fields) > 1:
            self.max_minute = int(numbers_only.findall(max_time_fields[1])[0])
        
        is_am = time_range[0].strip().endswith('am')
        is_pm = time_range[0].strip().endswith('pm')
        if (is_pm and self.min_hour < 12) \
            or is_am and self.min_hour == 12:
            self.min_hour += 12

        is_am = time_range[1].strip().endswith('am')
        is_pm = time_range[1].strip().endswith('pm')
        if (is_pm and self.max_hour < 12) \
            or is_am and self.max_hour == 12:
            self.max_hour += 12
    
    def contains(self, check_time:time) -> bool:
        print("checking if restaurant ", self.name, " is open at ", check_time.hour,":",check_time.minute)
        print("restaurant is from", self.min_hour, " to ", self.max_hour)
        return (check_time.hour > self.min_hour and check_time.hour < self.max_hour) \
            or (check_time.hour == self.min_hour) \
            or (check_time.hour == self.max_hour and check_time.minute == 0)
