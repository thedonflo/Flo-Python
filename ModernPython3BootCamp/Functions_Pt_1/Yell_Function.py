# Yell Function Exercise
# Implement a function yell  which accepts a single string argument.
# It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  For example:
#
# yell("go away")   # "GO AWAY!"
#
# yell("leave me alone")   # "LEAVE ME ALONE!"
#
# You do not need to call the function to pass the tests.
#
# Remember, that currently you can't use f-strings in Udemy coding challenges, so either use string concatenation or the format() method.
#


def yell(command):
    return command.upper()+'!'

print(yell('leave me alone'))
