DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
PM_OR_AM = "AM"


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

    # If the total time is greater than 24 it adds to the amount of days ahead
    days_added = 0
    if total_time_decimal > 24:
        days_added += int(total_time_decimal // 24)
        total_time_decimal -= (24 * days_added)

    # If the time is greater than 12 the time is in PM
    if total_time_decimal > 12:
        total_time_decimal -= 12
        if int(total_time_decimal) != 0:
            global PM_OR_AM
            PM_OR_AM = "PM"

    # If the time is 12 then it should change the time to PM
    if round(total_time_decimal) == 12:
        PM_OR_AM = "PM"

    # Converts the time decimal into digital time
    time = decimal_to_time(total_time_decimal)

    print(days_added)

    # Checks if starting day exists
    if starting_day:
        formatted_day = starting_day.capitalize()
        day_index = DAYS_OF_THE_WEEK.index(formatted_day)
        new_index = day_index + days_added

        # Checks if days added is less than 1
        if days_added == 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM}, {DAYS_OF_THE_WEEK[day_index + 1]} (next day)"

        # Checks if the new_index is greater than the last index of the DAYS_OF_THE_WEEK list
        if new_index > DAYS_OF_THE_WEEK.index(DAYS_OF_THE_WEEK[-1]):
            index_in_range = int(new_index // 7)
            return f"{time[0]}:{time[1]} {PM_OR_AM}, {DAYS_OF_THE_WEEK[index_in_range]} ({int(days_added)} days later)"

        if days_added > 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM}, {DAYS_OF_THE_WEEK[new_index]} ({int(days_added)} days later)"

    # Checks if starting day doesn't exist
    if not starting_day:
        # Checks if days added is 1
        if days_added == 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM} (next day)"

        # Checks if days added is less than 1
        if days_added < 1:
            return f"{time[0]}:{time[1]} {PM_OR_AM}"

        # Checks if days added is greater than 1
        if days_added > 1:
            print("trigged1")
            return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} days later)"

        return f"{time[0]}:{time[1]} {PM_OR_AM} ({int(days_added)} day later)"
    else:
        formatted_day = starting_day.capitalize()
        day_index = DAYS_OF_THE_WEEK.index(formatted_day)
        new_index = day_index + days_added
        if new_index > DAYS_OF_THE_WEEK.index(DAYS_OF_THE_WEEK[-1]):
            index_in_range = int(new_index // 7)

            return f"{time[0]}:{time[1]} {PM_OR_AM}, {DAYS_OF_THE_WEEK[index_in_range]} ({int(days_added)} days later)"
        else:
            return f"{time[0]}:{time[1]} {PM_OR_AM}, {formatted_day}"


print(add_time('8:16 PM', '466:02', 'tuesday'))
