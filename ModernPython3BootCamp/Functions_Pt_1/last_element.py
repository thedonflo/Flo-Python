# Write a function called last_element.
# This function takes in one parameter (a list) and returns the last value in the list.
# It should return None if the list is empty.
#
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(input):
    if input:
        return input[-1]
    return None

last_element([1,2,3])
last_element([])