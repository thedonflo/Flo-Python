# get_multiples
# Write a function called get_multiples, which accepts a number and a count,
# and returns a generator that yields the first count multiples of the number.
#
# The default number should be 1, and the default count should be 10.


def get_multiples(number=1, count=10):
    for i in range(count):
        yield number * (i+1)

# evens = get_multiples(2, 3)
# print(next(evens)) # 2
# print(next(evens)) # 4
# print(next(evens)) # 6
# print(next(evens)) # StopIteration

default_multiples = get_multiples()
print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]