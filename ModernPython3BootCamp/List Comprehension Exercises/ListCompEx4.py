#Given the string "amazing" create a variable called answer, which is a list containing all the letters from "amazing" but not the vowels(a,e,i,o,u).
#The answer should look like:['m','z','n','g']
#Use a list comprehension

answer = [char for char in "amazing" if char not in "a,e,i,o,u"]
print(answer)


