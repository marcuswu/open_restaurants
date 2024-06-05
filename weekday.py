from enum import Enum

class Weekday(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    @classmethod
    def of(cls, day:str):
        upper_day = day.upper()
        if upper_day.startswith("SU"):
            return Weekday.SUNDAY
        if upper_day.startswith("M"):
            return Weekday.MONDAY
        if upper_day.startswith("TH"):
            return Weekday.THURSDAY
        if upper_day.startswith("T"):
            return Weekday.TUESDAY
        if upper_day.startswith("W"):
            return Weekday.WEDNESDAY
        if upper_day.startswith("F"):
            return Weekday.FRIDAY
        if upper_day.startswith("SA"):
            return Weekday.SATURDAY
        return None