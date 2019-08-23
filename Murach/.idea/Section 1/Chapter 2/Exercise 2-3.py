#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

# calculate miles per gallon
area = int(length * width)
perimeter = int((2 * length) + (2 * width))

# format and display the result
print()
print("Area = " + str(area))
print("Perimeter = " + str(perimeter))
print()
print("Thanks for using this program!")


