# This makes it easier to read the timer for elapsed times that are less than one day.
# Review the code and test it
# 1. In IDLE, open the timer.py file that's in this folder:
# python/ exercises/ ch11

# 2. Review the code and run the program to see how it works.
# Modify the way the elapsed time is displayed
# 3. Modify the code that displays the start and stop times so it only displays the
# time part, not the date part.
# 4. Modify the code that displays the elapsed time so it only shows hours/minutes
# and seconds. Also, the program should only display the hours/minutes data if
# it contains a non-zero value.


#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    # print(start_time.time())
    print("Start time:", start_time.strftime("%X.%f"))
    print()

    # stop timer
    input("Press Enter to stop...")
    stop_time = datetime.now()
    # print(stop_time.time())
    print("Stop time: ", stop_time.strftime("%X.%f"))
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if days > 0:
        print("Days:", days)
    # print("Time:", time_object)
    else:
        if hours > 0 or minutes > 0:
            print(f"Hours/minutes: {time_object.strftime('%H:%M')}")
        print(f"Seconds: {time_object.strftime('%S.%f')}") #%S%f

if __name__ == "__main__":
    main()
