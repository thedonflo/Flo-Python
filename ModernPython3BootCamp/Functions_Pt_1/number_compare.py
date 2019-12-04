# Write a function called number_compare. This function takes in two parameters (both numbers).
# If the first is greater than the second,
# this function returns "First is greater"
# If the second number is greater than the first,
# the function returns "Second is greater." Otherwise the function returns "Numbers are equal"
#

# '''
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,0) # "First is greater"
# number_compare(2,4) # "Second is greater"
# '''

def number_compare(input1, input2):
    if input1 > input2:
        return "First is greater"
    elif input2 > input1:
        return "Second is greater"
    return "Numbers are equal"

print(number_compare(1,1))
print(number_compare(1,0))
print(number_compare(2,4))
