#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

choice = "y"
while choice.lower() == "y":
# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cpg = float(input("Enter cost per gallon:     "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cpg <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gas = round((gallons_used * cpg), 2)
        cost_per_mile = round((total_gas / miles_driven), 2)

        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:           ", total_gas)
        print("Cost Per Mile:            ", cost_per_mile)
        print()
    choice = input("Get entries for another trip (y/n)? ")
    print()




