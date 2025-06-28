def resultado():
    print(f'\n\
Final result: {\
            add_time(\
            test_start,\
            test_duration,\
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
test_start, test_duration = '3:00 PM', '3:10'
# test_start, test_duration, test_weekday = '11:30 AM', '2:32', 'Monday'
# test_start, test_duration = '10:10 PM', '3:30'
# test_start, test_duration, test_weekday = '11:43 PM', '24:20', 'tueSday'
# test_start, test_duration = '6:30 PM', '205:12'

TIME = {
    'hour': int(),
    'minute': int(),
    'meridiem': str(),
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
    'hour': int(),
    'minute': int()
}

def init(time_str, day=None):
    """Parse a time string in the format 'HH:MM AM/PM' or 'HH:MM'."""
    h_m_M = time_str.strip().strip("',").split()

    if len(h_m_M) > 1: # then it's a start time with AM/PM
        # save the meridiem before splitting
        TIME['meridiem'] = str(h_m_M[1]).upper()

        h_m = h_m_M[0].split(':')
        TIME['hour'] = int(h_m[0])
        TIME['minute'] = int(h_m[1])

    else: # it's a DURATION[] time without AM/PM
        h_m = h_m_M[0].split(':')
        DURATION['hour'] = int(h_m[0])
        DURATION['minute'] = int(h_m[1])

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

def fix_overflow_in(time, to = {'over_hours', 'days_later'}):
    """Check if minutes, hours, days overflow and adjust accordingly."""

    what_to_fix = to

    if what_to_fix == {'days_later'}:
        hour = time
        if hour >= 24:
            overflow_days = hour // 24
            hour = hour % 24
            return hour, overflow_days
        return hour, 0

    if what_to_fix == {'over_hours'}:
        minute = time
        if minute >= 60:
            overflow_hours = minute // 60
            minute = minute % 60
            return minute, overflow_hours
        return minute, 0

def how_many(days_later):
    """Return a string indicating how many days_later."""
    match days_later:
        case 1: return ' (next day)'

    return f' ({days_later} days later)'

def add_time(start, duration, day=None):
    if day:
        day = day.lower().capitalize()
        init(start, day)
        start_day = TIME['day'].index(day)
    else:
        init(start)
    init(duration)

    print(f'Start hour: {TIME["hour"]}, Start minute: {TIME["minute"]}, Start period: {TIME["meridiem"]}, Start day: {TIME["day"] if day else "Day not provided"}')

    # Convert 12'clock to 24'clock and start doing operations
    TIME['hour'] = clock_12_to_24(TIME['hour'], TIME['meridiem'])

    TIME['hour'] += DURATION['hour']
    TIME['minute'] += DURATION['minute']

    TIME['minute'], over_hours = fix_overflow_in(TIME['minute'], to={'over_hours'})

    TIME['hour'] += over_hours

    TIME['hour'], days_later = fix_overflow_in(TIME['hour'], to={'days_later'})

    TIME['hour'], TIME['meridiem'] = clock_24_to_12(TIME['hour'])
    # Finished operations and converted back to 12'clock, now define the new time
    new_time = f'{TIME["hour"]}:{TIME["minute"]:02d} {TIME["meridiem"]}'
    if day:
        new_time += f', {TIME["day"][(start_day + days_later) % 7]}'
    if days_later > 0:
        new_time += how_many(days_later)

    return new_time

if __name__ == '__main__':
    resultado()
