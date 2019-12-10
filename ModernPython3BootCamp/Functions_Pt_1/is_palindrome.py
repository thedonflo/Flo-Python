# Write a function called is_palindrome.
# A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
# This function should take in one parameter and returns True or False depending on whether it is a palindrome.
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
#

# '''
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True


def is_palindrome(review):
    review = review.replace(" ","").lower()
    collection = list(review)
    switch = collection.copy()
    switch.reverse()
    return collection == switch


print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True


# print(is_palindrome('tacocat'))

# review = "a man a plan a canal  Panama"
# review = review.replace(" ","").lower()
# print(review)
# collection = list(review)
# switch = collection.copy()
# switch.reverse()
# print(collection)
# print(switch)
# print(collection == switch)
