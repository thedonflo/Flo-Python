'''
Write a function called compact.
This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]
'''

#1st Solution
# def compact(collection):
#     buildlist = []
#     for collect in collection:
#         if collect:
#             buildlist.append(collect)
#     return buildlist


#2nd Solution
def compact(collection):
    return [collect for collect in collection if collect]



print(compact([0,1,2,"",[], False, {}, None, "All done"]))