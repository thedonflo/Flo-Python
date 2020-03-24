# In this exercise, you'll modify the Future Value program so the user can't cause
# the program to crash by entering an invalid int or float value.
# 1. In IDLE, open the future_value.py file that's in this folder:
# python/ exercises/ ch08
# 2. Review the code and study the get_ valid_number() and get_ valid_integer()
# functions. Note that they receive three arguments: the prompt for a user entry,
# the low value that the entry must be greater than, and the high value that the
# entry must be less than or equal to. Then, review the calling statements in the
# main() function and note how these functions are used.
# 3. Test the program. Note that you can cause the program to crash by entering
# values that can't be converted to float and int values.
# 4. Add exception handling to the get_ valid_number() and get_ valid_integer()
# functions so the user has to enter valid float and int values. Then, test these
# changes to make sure the exception handling and the data validation work
# correctly.

#!/usr/bin/env python3

def get_number(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print("Entry must be greater than " + str(low)
                      + " and less than or equal to " + str(high) + ".")
        except ValueError:
            print("You entered an invalid float. Please try again")

def get_integer(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print("Entry must be greater than " + str(low)
                      + " and less than or equal to " + str(high) + ".")
        except ValueError:
            print("You entered an invalid integer. Please try again")


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
