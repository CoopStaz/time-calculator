DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
PM_OR_AM = "AM"


# Converts the time decimal into digital time
def decimal_to_time(decimal):
    hours = int(decimal)
    minutes = round((decimal - hours) * 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    return hours, minutes


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
    print(start_time_decimal)

    # Calculates the duration times
    duration_array = duration.split(":")

    duration_hour = int(duration_array[0])
    duration_minute = int(duration_array[1]) / 60
    print(duration_minute)

    duration_time_decimal = duration_hour + duration_minute

    # Gets the sum of both the start time and the duration time to get the new time in decimal form
    total_time_decimal = start_time_decimal + duration_time_decimal

    # If the total time is greater than 24 it adds to the amount of days ahead
    days_added = 0
    if total_time_decimal > 24:
        days_added += total_time_decimal // 24
        total_time_decimal -= (24 * days_added)

    # If the time is greater than 12 the time is in PM
    if total_time_decimal > 12:
        total_time_decimal -= 12
        if int(total_time_decimal) != 0:
            global PM_OR_AM
            PM_OR_AM = "PM"

    # Converts the time decimal into digital time
    time = decimal_to_time(total_time_decimal)

    if not starting_day:
        if days_added < 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM}"
        else:
            if days_added > 1:
                return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} days later)"
            else:
                return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} day later)"
    else:
        formatted_day = starting_day.capitalize()
        day_index = DAYS_OF_THE_WEEK.index(formatted_day)
        new_index = day_index + days_added

        if new_index > DAYS_OF_THE_WEEK.index(DAYS_OF_THE_WEEK[-1]):
            index_in_range = int(new_index // 7)
            return f"{time[0]}:{time[1]} {PM_OR_AM}, {DAYS_OF_THE_WEEK[index_in_range]} ({int(days_added)} days later)"


print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
