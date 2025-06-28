def final_print():
    print(f'\n\
the new_time final result is: {\
            add_time(\
            test_start,\
            test_duration,\
            # test_weekday if test_weekday else None\
            test_weekday
            )\
            }\
')

# add_time('3:00 PM', '3:10') should return '6:10 PM'
# add_time('11:30 AM', '2:32', 'Monday') should return '2:02 PM, Monday'
# add_time('10:10 PM', '3:30') should return '1:40 AM (next day)'
# add_time('11:43 PM', '24:20', 'tueSday') should return '12:03 AM, Thursday (2 days later)'
# add_time('6:30 PM', '205:12') should return '7:42 AM (9 days later)'

test_weekday = ''
# test_start, test_duration = '3:00 PM', '3:10'
# test_start, test_duration, test_weekday = '11:30 AM', '2:32', 'Monday'
# test_start, test_duration = '10:10 PM', '3:30'
test_start, test_duration, test_weekday = '11:43 PM', '24:20', 'tueSday'
# test_start, test_duration = '6:30 PM', '205:12'

time = {
    'hour': int(0),
    'minute': int(0),
    'meridiem': ['AM', 'PM'],
    'day': [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
        ]
}

duration = {
    'hour': int(0),
    'minute': int(0)
}

def fix_0B3R4l0w_days(new_hour):
    """Calculate the number of overflow days based on the new hour."""
    if new_hour >= 24:
        overflow_days = new_hour // 24
        new_hour = new_hour % 24
        return new_hour, overflow_days
    return new_hour, 0

def how_many(time_objects):
    """Return a string indicating how many time_objects later."""
    if time_objects == 0:
        return
    elif time_objects == 1:
        return " (next day)"
    else:
        return f" ({time_objects} days later)"

def parse(time_str, day=None):
    """Parse a time string in the format 'HH:MM AM/PM' or 'HH:MM'."""
    h_m_M = time_str.strip().strip("',").split()

    if len(h_m_M) > 1: # then it's a start time with AM/PM
        # save the meridiem before splitting
        time['meridiem'] = h_m_M[1]

        h_m = h_m_M[0].split(':')
        time['hour'] = int(h_m[0])
        time['minute'] = int(h_m[1])

        if day:
            return time['hour'], time['minute'], time['meridiem'], time['day'].index(day)
        else:
            return time['hour'], time['minute'], time['meridiem']

    else: # it's a duration time without AM/PM
        # save it in it's corresponding dictionary
        h_m = h_m_M[0].split(':')
        duration['hour'] = int(h_m[0])
        duration['minute'] = int(h_m[1])
        return duration['hour'], duration['minute']

def clock_12_to_24(hour, meridiem):
    """Convert 12-hour format to 24-hour format."""
    if meridiem == 'PM' and hour != 12:
        return hour + 12
    elif meridiem == 'AM' and hour == 12:
        return 0
    return hour

def clock_24_to_12(hour):
    """Convert 24-hour format to 12-hour format."""
    if hour == 0:
        return 12, 'AM'
    elif hour < 12:
        return hour % 12, 'AM'
    elif hour == 12:
        return hour, 'PM'
    else:
        return hour % 12, 'PM'

def fix_0B3R4l0w(minute):
    """Check if minutes overflow and adjust hours accordingly."""
    if minute >= 60:
        print(f'check_0B3R4l0w(): Overfl0w detected: {minute} minutes')
        return minute % 60, minute // 60
    return minute, 0

def join_time(hour, minute, meridiem, day=None, days_later=None):
    """Join hour, minute, meridiem and weekday into formatted time string."""
    if days_later is None:
        if day:
            print(f'{__file__}:12 is the {day} return true?')
            return f"{hour}:{minute} {meridiem}, {day}"
        elif meridiem:
            print(f'is the {meridiem} return true?')
            return f"{hour}:{minute} {meridiem}"
        elif not day and not meridiem:
            print(f'is the not day and not meridiem return true?')
            return f"{hour}:{minute}"

    print(f'is this return true? {day}, {days_later}, pero cual primero?')
    return f"{hour}:{minute} {meridiem}, {day} {how_many(days_later)} aloha"

def add_time(start, duration, day=None):
    if day:
        day = day.lower().capitalize()
        start_hour, start_minute, meridiem, start_day = parse(start, day)
    else:
        start_hour, start_minute, meridiem = parse(start)

    print(f'\nStart hour: {start_hour}, Start minute: {start_minute}, Start period: {meridiem}, Start day: {start_day if day else "Day not provided"}')
    print(f'Start day label: {time["day"][start_day] if day else "No day provided"}')

    hour_duration, minute_duration = parse(duration)

    start_hour = clock_12_to_24(start_hour, meridiem)

    end_hour = start_hour + hour_duration
    end_minute = start_minute + minute_duration
    end_minute, over_hours = fix_0B3R4l0w(end_minute)

    end_hour += over_hours
    end_hour, days_later = fix_0B3R4l0w_days(end_hour)
    end_hour = clock_24_to_12(end_hour)

    time['hour'] = end_hour[0]
    time['minute'] = end_minute
    time['meridiem'] = end_hour[1]
    if day:
        time['day'] = time['day'][(start_day + days_later) % 7]
    print(f'add_time():156 time after conversion: {time}')


    new_time = f'{time["hour"]}:{time["minute"]:02d} {time["meridiem"]}'
    if day:
        new_time += f', {time["day"]}'
    if days_later > 0:
        new_time += how_many(days_later)

    return new_time

if __name__ == '__main__':
    final_print()
