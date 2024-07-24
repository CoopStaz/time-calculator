DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
PM_OR_AM = "AM"

# Converts the time decimal into digital time
def decimal_to_time(decimal):
    hours = int(decimal)
    minutes = (decimal - hours) * 60
    return hours, int(minutes)


def add_time(start, duration, starting_day=None):
    # Calculates the start times
    start_array = start.split(" ")
    start_time_array = start_array[0].split(":")

    start_hour = int(start_time_array[0])
    # Add 12 hours to the time hours if it is in PM time
    if start_array[1] == "PM":
        start_hour += 12
    start_minute = int(start_time_array[1]) / 60

    start_time_decimal = start_hour + start_minute

    # Calculates the duration times
    duration_array = duration.split(":")

    duration_hour = int(duration_array[0])
    duration_minute = int(duration_array[1]) / 60

    duration_time_decimal = duration_hour + duration_minute

    # Gets the sum of both the start time and the duration time to get the new time in decimal form
    total_time_decimal = start_time_decimal + duration_time_decimal
    print(total_time_decimal)

    # If the total time is greater than 24 it adds to the amount of days ahead
    days_added = 0
    if total_time_decimal > 24:
        days_added += total_time_decimal // 24
        print(days_added)
        total_time_decimal -= (24 * days_added)

    # If the time is greater than 12 the time is in PM
    if total_time_decimal > 12:
        total_time_decimal -= 12
        if int(total_time_decimal) != 0:
            global PM_OR_AM
            PM_OR_AM = "PM"

    # Converts the time decimal into digital time
    time = decimal_to_time(total_time_decimal)
    print(time)

    if not starting_day:
        if days_added < 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM}"
        else:
            if days_added > 1:
                return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} days later)"
            else:
                return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} day later)"
    else:
        day_index = DAYS_OF_THE_WEEK.index(starting_day)
        # Do the starting day functionality


print(add_time('6:14 AM', '25:32'))
