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
# test_start, test_duration, test_weekday = '11:43 PM', '24:20', 'tueSday'
test_start, test_duration = '6:30 PM', '205:12'

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

DURATION = {
    'hour': int(0),
    'minute': int(0)
}

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

def how_many(time_objects):
    """Return a string indicating how many time_objects later."""
    if time_objects == 0:
        return
    elif time_objects == 1:
        return " (next day)"
    else:
        return f" ({time_objects} days later)"

def fix_0B3R4l0w(minute):
    """Check if minutes overflow and adjust hours accordingly."""
    if minute >= 60:
        print(f'check_0B3R4l0w():77 Overfl0w detected: {minute} minutes')
        return minute % 60, minute // 60
    return minute, 0

def fix_0B3R4l0w_days(new_hour):
    """Calculate the number of overflow days based on the new hour."""
    if new_hour >= 24:
        overflow_days = new_hour // 24
        new_hour = new_hour % 24
        return new_hour, overflow_days
    return new_hour, 0

def parse(time_str, day=None):
    """Parse a time string in the format 'HH:MM AM/PM' or 'HH:MM'."""
    h_m_M = time_str.strip().strip("',").split()

    if day:
        day = day.lower().capitalize()
        # print(f'parse():95 time["day"] type: {type(time["day"])}')
        # time['day'] = time['day'].index(day)
        # print(f'parse():97 time["day"]: {time["day"]}')
        # print(f'parse():98 time["day"] type: {type(time["day"])}')

    if len(h_m_M) > 1: # then it's a start time with AM/PM
        # save the meridiem before splitting
        print(f'parse():102 time["meridiem"]: {time["meridiem"]}')
        print(f'parse():103 time["meridiem"] tyep: {type(time["meridiem"])}')
        time['meridiem'] = h_m_M[1]
        print(f'parse():105 time["meridiem"]: {time["meridiem"]}')
        print(f'parse():106 time["meridiem"] type: {type(time["meridiem"])}')

        h_m = h_m_M[0].split(':')
        time['hour'] = int(h_m[0])
        time['minute'] = int(h_m[1])

    else: # it's a DURATION[] time without AM/PM
        h_m = h_m_M[0].split(':')
        DURATION['hour'] = int(h_m[0])
        DURATION['minute'] = int(h_m[1])

def add_time(start, duration, day=None):
    # if day:
    #     day = day.lower().capitalize()
    #     start_hour, start_minute, meridiem, start_day = parse(start, day)
    # else:
    #     start_hour, start_minute, meridiem = parse(start)
    #
    # print(f'\nStart hour: {start_hour}, Start minute: {start_minute}, Start period: {meridiem}, Start day: {start_day if day else "Day not provided"}')
    # print(f'Start day label: {time["day"][start_day] if day else "No day provided"}')
    #
    # hour_duration, minute_duration = parse(duration)

    if day:
        day = day.lower().capitalize()
        parse(start, day)
        start_day = time['day'].index(day)
    else:
        parse(start)

    print(f'Start hour: {time["hour"]}, Start minute: {time["minute"]}, Start period: {time["meridiem"]}, Start day: {time["day"] if day else "Day not provided"}')

    parse(duration)

    print(f'time["meridiem"]: {time["meridiem"]}')
    time['hour'] = clock_12_to_24(time['hour'], time['meridiem'])

    time['hour'] += DURATION['hour']
    time['minute'] += DURATION['minute']
    time['minute'], over_hours = fix_0B3R4l0w(time['minute'])

    time['hour'] += over_hours
    time['hour'], days_later = fix_0B3R4l0w_days(time['hour'])
    print(f'add_time():149 days_later: {days_later}')
    print(f'add_time():150 days_later type: {type(days_later)}')

    time['hour'], time['meridiem'] = clock_24_to_12(time['hour'])

    if day:
        print(f'add_time():153 time["day"].index(day) type: {type(time["day"].index(day))}')
        print(f'time["day"]: {time["day"]}')
        print(f'{time["day"].index(day)}')
        # time['day'] += time['day'][(start_day + days_later) % 7]
        # time['day'] = time['day'][(time['day'].index(day) + days_later) % 7]
    print(f'add_time():160 time after conversion: {time}')


    new_time = f'{time["hour"]}:{time["minute"]:02d} {time["meridiem"]}'
    if day:
        new_time += f', {time["day"][(start_day + days_later) % 7]}'
    if days_later > 0:
        new_time += how_many(days_later)

    return new_time

if __name__ == '__main__':
    final_print()
