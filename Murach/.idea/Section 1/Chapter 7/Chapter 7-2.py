# 1. In IDLE, open the mpg.py file that's in this folder:
# python/exercises/ch07
# 2. Add a write_trips() function that writes the data from a two-dimensional list
# named trips that's passed to it as an argument. This list contains the data for
# each trip that's entered, and it should be written to a CSV file named trips.csv.
# As the console above shows, the data for each trip consists of miles driven,
# gallons of gas used, and the calculated MPG value.
# 3. Add a read_trips() function that reads the data from the trips.csv file and
# returns the data for the trips in a two-dimensional list named trips.
# 4. Add a list_trips() function that displays the data in the trips list on the console,
# as shown above.
# 5. Enhance the main() function so it starts by getting the data from the CSV file
# and listing it as shown above.
# 6. Enhance the main() function so it adds the last trip that's entered to the trips
# list after it calculates the MPG. Then, display the data for the updated trips
# list.
# 7. Test all aspects of the program until you 're sure that it works correctly.

#!/usr/bin/env python3
import csv
FILENAME = "trips.csv"
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

def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def read_trips():
    trips = []
    with open(FILENAME, newline="" ) as file:
        reader= csv.reader(file)
        for row in reader:
            trips.append(row)
        return trips


def list_trips(trips):
    print('Distance\tGallons\t\tMPG')
    for i in range(len(trips)):
        trip = trips[i]
        print(str(trip[0])+"\t\t"+ str(trip[1])+"\t\t"+str(trip[2]))

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        trips = read_trips()
        list_trips(trips)
        print()
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        miles = [miles_driven,gallons_used,mpg]
        trips.append(miles)
        write_trips(trips)
        list_trips(trips)

        more = input("More entries? (y or n): ")
    print("Bye")

if __name__ == "__main__":
    main()