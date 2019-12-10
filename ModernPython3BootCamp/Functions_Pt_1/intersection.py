'''
Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.

intersection([1,2,3], [2,3,4])    #[2,3]
intersection(['a','b','z'], ['x','y','z']) .  # ['z']
'''

#1st Solution
# def intersection(collection1, collection2):
#     buildup = []
#     for collect1 in collection1:
#         for collect2 in collection2:
#             if collect1 == collect2:
#                 buildup.append(collect1)
#     return buildup


#2nd Solution
def intersection(collection1, collection2):
    return [collect1 for collect1 in collection1 if collect1 in collection2]

print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','z'], ['x','y','z']))