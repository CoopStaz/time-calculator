# Time Calculator
A function named add_time that takes in two required parameters and one optional parameter. The function should add the duration time to the start time and return the result.

The parameters are as following:
1. start, a start time in the 12-hour clock format (ending in AM or PM)
2. duration, a duration time that indicates the number of hours and minutes added to the start time
3. **(optional)** starting_day, a starting day of the week which is case insensitive

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
