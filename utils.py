import re
from weekday import Weekday

def days_for_range(weekday_range:str) -> list[Weekday]:
    ret = []
    for day in weekday_range.split(','):
        day_range = day.split('-')
        if len(day_range) < 2:
            day = Weekday.of(day_range[0].strip())
            if day == None:
                continue
            ret.append(day)
        else:
            start = Weekday.of(day_range[0].strip())
            end = Weekday.of(day_range[1].strip())
            if start == None or end == None:
                continue
            for i in range(start.value, end.value+1):
                ret.append(Weekday(i))
    return ret


def split_hours(hours:str) -> list[tuple[str, str]]:
    res = []
    # Build up regular expression to capture day and hour ranges
    # Separated out to be easier to write and understand, but also for reuse
    sun_regex = "[Ss]u(?:n|nday)?"
    mon_regex = "[Mm](?:on|onday)?"
    thu_regex = "[Tt]h(?:ur|urs|ursday)?"
    tue_regex = "[Tt]u(?:e|es|esday)?"
    wed_regex = "[Ww](?:ed|ednesday)?"
    fri_regex = "[Ff](?:r|ri|riday)?"
    sat_regex = "[Ss]a(?:t|turday)?"

    # A day
    day_regex = "(?:{}|{}|{}|{}|{}|{}|{})".format(sun_regex, mon_regex, thu_regex, tue_regex, wed_regex, fri_regex, sat_regex)
    # A day or a range of days
    day_range_regex = r'(?:{}\s*(?:-\s*{})?)'.format(day_regex, day_regex, day_regex)
    # a list of days or ranges of days
    day_ranges_regex = r'{}(?:,\s*{})*'.format(day_range_regex, day_range_regex)
    # a time
    time_regex = r'[0-2]?[0-9](?::[0-6][0-9])?\s*(?:(?:am)|(?:pm))?'
    # a time range
    time_range_regex = r'{}\s*-\s*{}'.format(time_regex, time_regex)
    # the full day and hour range regular expression
    hours_regex = r'{}\s*{}\s*'.format(day_ranges_regex, time_range_regex)
    split_regex = r'(?P<day_range>{})\s*(?P<time_range>{})'.format(day_ranges_regex, time_range_regex)
    
    pattern = re.compile(hours_regex)
    split_pattern = re.compile(split_regex)

    # We now have a list of the day ranges -- something like:
    #  ['Mon-Thu, Sun 11:30 am - 10 pm', 'Fri 11 am - 11 pm', 'Sat 7 am - 12 pm']
    for rangeset in pattern.findall(hours):
        print(rangeset)
        # Split the day and time range
        m = split_pattern.search(rangeset)
        res.append((m.group('day_range'), m.group('time_range')))
    return res

