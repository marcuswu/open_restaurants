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
        if day.startswith("Su"):
            return Weekday.SUNDAY
        if day.startswith("M"):
            return Weekday.MONDAY
        if day.startswith("Th"):
            return Weekday.THURSDAY
        if day.startswith("T"):
            return Weekday.TUESDAY
        if day.startswith("W"):
            return Weekday.WEDNESDAY
        if day.startswith("F"):
            return Weekday.FRIDAY
        if day.startswith("Sa"):
            return Weekday.SATURDAY
        return None