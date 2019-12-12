'''
Map Time Exercise
Write a function called decrement_list  that accepts a single list of numbers as a parameter.
It should return a copy of the list where each item has been decremented by one. Use map to do this! For example:

decrement_list([1,2,3])   #[0,1,2]

decrement_list([20,14,11])  #[19,13,10]

Tips:

Remember map doesn't return a list on its own.  decrement_list , however, should return a list.
You can either pass map another name function or use a lambda.  A lambda is preferable, even if it is a little scary looking.
'''


def decrement_list(numbers):
    return list(map(lambda x: x - 1, numbers))


print(decrement_list([1,2,3]))   #[0,1,2]

print(decrement_list([20,14,11]))  #[19,13,10]