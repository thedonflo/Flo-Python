#!/usr/bin/env python3
# 1. In IDLE, open the 1npg_write.py file that's in this folder:
# python/exercises/ch07
# 2. Review the code, and run the progra1n so you re1ne1nber how it works.
# 3. Enhance the progra1n so it stores the data for each calculation, or trip, in a
# two-di1nensional list. For each calculation, these values should be put in the
# list: miles driven, gallons of gas used, and the calculated MPG value.
# 4. Enhance the progra1n so it saves the data in the list to a file named trips.csv
# when the user wants to exit from the program.
# 5. Test the program to 1nake sure it works. To do that, you can open the CSV file
# with a spreadsheet progra1n like Excel.
import csv

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    total_miles = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        miles = [miles_driven,gallons_used,mpg]
        total_miles.append(miles)
        more = input("More entries? (y or n): ")

    print(total_miles)
    with open("trips.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(total_miles)
    print("Bye")

if __name__ == "__main__":
    main()

