# Given a person variable:
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#
# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.
# That's a terrible explanation.  I think it'll be easier if you just look at the end goal:
#
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
# There are many potential solutions for this.
#
#

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer

answer = {person[i][0]: person[i][1] for i in range(0,len(person))}
# print(person[2][1])
# If you have a list of pairs, you can very easily turn it into a dictionary using dict()
# answer = dict(person)
print(answer)