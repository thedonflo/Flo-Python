# Generating Evens Exercise
# This exercise is a little harder than the previous make_noise  function.
#
# Write a function called generate_evens  that returns a list of the even numbers between 1 and 50(not including 50).
# Basically, it should return a list: [2,4,6....all the way up to 48]
# Inside the function, you can construct the list using either a loop OR list comprehension.
# You do not need to call the function in this exercise, defining it is enough.


#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

def generate_evens():
    num_list = []
    for i in range(1,50):
        if i % 2 == 0:
            num_list.append(i)
    return num_list

print(generate_evens())