#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cpg = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
total_gas_cost = float(gallons_used * cpg)
cpm = total_gas_cost//mpg

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t\t" + str(total_gas_cost))
print("Cost Per Mile:\t\t\t" + str(((cpg*gallons_used)/miles_driven)))


