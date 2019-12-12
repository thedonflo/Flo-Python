'''
Filter Exercise!
Write a function called remove_negatives that accepts a list of numbers and returns a copy of the lists with all negative numbers removed.
Use filter() in your implementation, not a list comprehension!

remove_negatives([-1,3,4,-99])     #[3,4]

remove_negatives([-7,0,1,2,3,4,5])      #[0, 1, 2, 3, 4, 5]

remove_negatives([50,60,70])   #[50,60,70]

HINTS

Make sure you return a list!  Remember filter does not return a list! You have to convert the result to a list yourself.
Note that 0 is not considered negative, so it should not be filtered out!
'''


def remove_negatives(negatives):
    return list(filter(lambda x: x>=0, negatives))

print(remove_negatives([-1,3,4,-99]))   #[3,4]

print(remove_negatives([-7,0,1,2,3,4,5]))      #[0, 1, 2, 3, 4, 5]

print(remove_negatives([50,60,70]))   #[50,60,70]