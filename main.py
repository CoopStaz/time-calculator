DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Converts the time decimal into digital time
def decimal_to_time(decimal):
    hours = int(decimal)
    minutes = round((decimal - hours) * 60)

    # Ensure there is a 0 in front of the number if it is single digit
    if minutes < 10:
        minutes = f"0{minutes}"

    # If it is midnight, change the time from 00 to 12
    if hours == 0:
        hours = 12

    return hours, minutes


def add_time(start, duration, starting_day=None):
    # Calculates the start times
    start_array = start.split(" ")
    start_time_array = start_array[0].split(":")

    start_hour = int(start_time_array[0])
    start_minute = int(start_time_array[1]) / 60
    print(start_hour)

    # Add 12 hours to the time hours if it is in PM time and accounts for 12-hour cycles
    if start_array[1] == "PM" and start_hour != 12:
        start_hour += 12
    elif start_array[1] == "AM" and start_hour == 12:
        start_hour = 0
    print(start_hour)

    start_time_decimal = start_hour + start_minute

    # Calculates the duration times
    duration_array = duration.split(":")

    duration_hour = int(duration_array[0])
    duration_minute = int(duration_array[1]) / 60

    duration_time_decimal = duration_hour + duration_minute

    # Get the sum of both the start time and the duration time to get the new time in decimal form
    total_time_decimal = start_time_decimal + duration_time_decimal

    # Calculate days added and new time in decimal
    days_added = int(total_time_decimal // 24)
    total_time_decimal = total_time_decimal % 24

    # Determine AM or PM
    pm_or_am = "AM"
    if total_time_decimal >= 12:
        pm_or_am = "PM"
    if total_time_decimal >= 13:
        total_time_decimal -= 12
    if total_time_decimal == 12 or total_time_decimal == 0:
        pm_or_am = "PM" if pm_or_am == "AM" else "AM"
        if total_time_decimal == 0:
            total_time_decimal = 12

    # Converts the time decimal into digital time
    time = decimal_to_time(total_time_decimal)

    # Checks if starting day exists
    if starting_day:
        formatted_day = starting_day.capitalize()
        day_index = DAYS_OF_THE_WEEK.index(formatted_day)
        new_index = (day_index + days_added) % 7

        if days_added == 1:
            return f"{time[0]}:{time[1]} {pm_or_am}, {DAYS_OF_THE_WEEK[new_index]} (next day)"
        elif days_added > 1:
            return f"{time[0]}:{time[1]} {pm_or_am}, {DAYS_OF_THE_WEEK[new_index]} ({int(days_added)} days later)"
        else:
            return f"{time[0]}:{time[1]} {pm_or_am}, {formatted_day}"

    # Runs if starting day doesn't exist
    else:
        if days_added == 1:
            return f"{time[0]}:{time[1]} {pm_or_am} (next day)"

        elif days_added > 1:
            print("trigged1")
            return f"{time[0]}:{time[1]} {pm_or_am} ({int(days_added)} days later)"

        # Checks if days added is less than 1
        else:
            return f"{time[0]}:{time[1]} {pm_or_am}"


print(add_time('3:30 PM', '2:12', 'Monday'))
