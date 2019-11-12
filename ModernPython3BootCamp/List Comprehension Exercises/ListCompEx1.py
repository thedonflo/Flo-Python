#Given a list ["Ellie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.
#I would use a list comprehension, though you could also loop over manually.

#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.
#Anoter good candidate for a list comp.

answer = [name[0] for name in ["Ellie", "Tim", "Matt"]]
print(answer)

answer2 = [number for number in [1,2,3,4,5,6] if number % 2 == 0]
print(answer2)
