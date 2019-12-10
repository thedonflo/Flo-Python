# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(nums):
    start = 1
    for num in nums:
        if num % 2 == 0:
            start *= num
    return start


print(multiply_even_numbers([2,3,4,5,6]))