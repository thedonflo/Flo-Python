# Modify the CSV version of the write program
# 1. Open the mpg_ write.py file that you created in exercise 7-1. Then, save it as
# mpg_ write_binary.py in the same directory.
# 2. Modify this program so it saves the list as a binary file instead of a CSV file.
# The file should be named trips.bin.
# 3. Test the program to make sure it works. To do that, add statements that read
# the file at the end of the program and display the list that has been read.
# Modify the CSV version of the trip program
# 4. Open the mpg.py file that you created in exercise 7-2. Then, save it as
# mpg_binary. py.
# 5. Modify this program so it works the same as it did with the CSV file.
# 6. Test this program to make sure it works.

import pickle

FILENAME = 'trips.bin'

def write_trips(trips):
    with open(FILENAME, "wb") as file:
        pickle.dump(trips, file)

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

    trips = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        miles = [miles_driven,gallons_used,mpg]
        trips.append(miles)
        # print(total_miles)

        print(trips)
        more = input("More entries? (y or n): ")
    write_trips(trips)
    print('Distance\tGallons\t\tMPG')
    with open(FILENAME, "rb") as file:
        total_miles = pickle.load(file)
        print(total_miles)


    print("Bye")

if __name__ == "__main__":
    main()
