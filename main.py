# Converts the time decimal into digital time
def decimal_to_time(decimal):
    hours = int(decimal)
    minutes = (decimal - hours) * 60
    return hours, int(minutes)


def add_time(start, duration, starting_day=None):
    # TODO 1. Convert start and duration times to number of hours in a decimal and add their total.
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
        total_time_decimal -= 24 * days_added

    # TODO 2. Add a third parameter which is the starting day of the week.

    # TODO 3. Convert the hours back to times in AM or PM
    # Converts the time decimal into digital time
    time = decimal_to_time(total_time_decimal)
    print(time)

    # TODO 4. If result is more than a day later calculate what day it is

    # return new_time


add_time('11:30 AM', '2:32')
