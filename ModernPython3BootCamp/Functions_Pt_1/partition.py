'''
Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ).

The function should iterate over each element in the list and invoke the callback function at each iteration.

If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
When it's finished, partition should return both lists inside of one larger list, like so:

[truthy_list, falsy_list]

def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]

'''
def isEven(num):
    return num % 2 == 0
#1st Solution
# def partition(collection, string):
#     truthy_list = []
#     falsy_list = []
#     full_list = []
#     [truthy_list.append(num) if string(num) else falsy_list.append(num) for  num in collection]
#     full_list.append(truthy_list)
#     full_list.append(falsy_list)
#     return full_list


#2nd Solution
def partition(collection, string):
    return [[num for num in collection if string(num)], [num for num in collection if not string(num)]]
print(partition([1,2,3,4], isEven))