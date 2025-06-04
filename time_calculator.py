def add_time(start, duration, day=None):
    # Days of the week for lookup and index
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split start time into components
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Split duration into hours and minutes
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add minutes and carry over hours if needed
    total_minutes = start_minute + dur_minute
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60

    # Add hours including carried over hours from minutes
    total_hours = start_hour + dur_hour + extra_hours
    days_passed = total_hours // 24
    new_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if new_hour_24 == 0:
        new_hour = 12
        new_period = 'AM'
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = 'AM'
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = 'PM'
    else:
        new_hour = new_hour_24 - 12
        new_period = 'PM'

    # Determine new day of the week if provided
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        day_str = f", {new_day}"
    else:
        day_str = ""

    # Determine how many days later
    if days_passed == 1:
        day_later_str = " (next day)"
    elif days_passed > 1:
        day_later_str = f" ({days_passed} days later)"
    else:
        day_later_str = ""

    # Final formatted time string
    new_time = f"{new_hour}:{new_minute:02d} {new_period}{day_str}{day_later_str}"
    return new_time
