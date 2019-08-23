#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    is_invalid = True
    while is_invalid:
        monthly_investment = float(input("Enter monthly investment: "))
        if monthly_investment > 0:
            is_invalid = False
        else:
            print("Entry must be greater than 0. Please try again.")

    is_invalid = True
    while is_invalid:
        yearly_interest_rate = float(input("Enter yearly interest rate: "))
        if 0 <yearly_interest_rate <= 15:
                is_invalid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 15.\nPlease try again.")

    is_invalid = True
    while is_invalid:
        years = int(input("Enter number of years:\t"))
        if 0 < years <= 50:
            is_invalid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 50.\nPlease try again.")
            continue

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, months+1):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
        if i%12 == 0:
            print("Year = "+str(i//12)+" Future value:\t\t" + str(round(future_value, 2)))
    #print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
