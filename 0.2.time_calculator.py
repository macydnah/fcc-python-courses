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

    else: # it's a DURATION time without AM/PM
        h_m = h_m_M[0].split(':')
        DURATION['hour'] = int(h_m[0])
        DURATION['minute'] = int(h_m[1])

def clock(hour, meridiem, **convert_to):
    """Convert time between 12-hour and 24-hour formats."""
    for to in convert_to.values():
        match to:
            case '24-hour':
                if meridiem == 'PM' and hour != 12:
                    return hour + 12
                elif meridiem == 'AM' and hour == 12:
                    return 0
                return hour
            case '12-hour':
                if hour == 0:
                    return 12, 'AM'
                elif hour < 12:
                    return hour % 12, 'AM'
                elif hour == 12:
                    return hour, 'PM'
                else:
                    return hour % 12, 'PM'
            case _:
                raise ValueError("Invalid conversion type. Use convert_to='24-hour' or convert_to='12-hour'.")

def fix_overflow_in(time, **overflow):
    """Check if minutes, hours, days overflow and adjust accordingly."""
    for fix in overflow.values():
        match fix:
            case 'over_hours':
                minute = time
                if minute >= 60:
                    overflow_hours = minute // 60
                    minute = minute % 60
                    return minute, overflow_hours
                return minute, 0
            case 'days_later':
                hour = time
                if hour >= 24:
                    overflow_days = hour // 24
                    hour = hour % 24
                    return hour, overflow_days
                return hour, 0
            case _:
                raise ValueError("Invalid overflow type. Use to='over_hours' or to='days_later'.")

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

    print(f'Start hour: {TIME["hour"]}, Start minute: {TIME["minute"]}, Start period: {TIME["meridiem"]}, Start day: {TIME["day"][start_day] if day else "N/A"}')

    # Convert 12-hour to 24-hour clock and start doing operations
    TIME['hour'] = clock(TIME['hour'], TIME['meridiem'], convert_to='24-hour')

    TIME['hour'] += DURATION['hour']
    TIME['minute'] += DURATION['minute']

    TIME['minute'], over_hours = fix_overflow_in(TIME['minute'], to='over_hours')

    TIME['hour'] += over_hours

    TIME['hour'], days_later = fix_overflow_in(TIME['hour'], to='days_later')

    # 24-hour clocks have None meridiem
    TIME['hour'], TIME['meridiem'] = clock(TIME['hour'], None, convert_to='12-hour')
    # Converted back to 12-hour clock, now define the new time
    new_time = f'{TIME["hour"]}:{TIME["minute"]:02d} {TIME["meridiem"]}'
    if day:
        new_time += f', {TIME["day"][(start_day + days_later) % 7]}'
    if days_later > 0:
        new_time += how_many(days_later)

    return new_time
