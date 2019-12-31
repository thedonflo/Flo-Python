# Week Generator Exercise
# Write a function called week, which returns a generator that yields each day of the week,
# starting with Monday and ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.

# days = week()
# next(days) # 'Monday'
# next(days) # 'Tuesday'
# next(days) # 'Wednesday'
# next(days) # 'Thursday'
# next(days) # 'Friday'
# next(days) # 'Saturday'
# next(days) # 'Sunday'
# next(days) # StopIteration


def week():
    all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in all_days:
        yield day


# week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(len(week))
# counts = 0
# print(week[counts])
days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
# next(days) # 'Wednesday'
# next(days) # 'Thursday'
# next(days) # 'Friday'
# next(days) # 'Saturday'
# next(days) # 'Sunday'
# next(days) # StopIteration