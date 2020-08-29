# Open and test the program
# 1. In IDLE, open the two files stored in this folder:
# python/ exercises/ ch14 / temperature
# 2. Review the code for the program and note how it uses the functions in the
# temperature module to convert the temperatures.
# 3. Run the code to make sure it works correctly.
# Define a Temp object that can store a temperature
# 4. Switch to the temperature.py file. At the top of this module, define a class
#    named Temp that defines two hidden attributes to store the degrees Fahrenheit
# and Celsius.
# 5. In the Temp class, define the methods that set the hidden attributes. When you
# set one unit of temperature, it should also calculate and set the other unit of
# temperature. For example, when you set degrees Fahrenheit, it should also
# calculate and set degrees Celsius.
# 6. In the Temp class, define the methods that get the hidden attributes. These
# methods should round the number that it returns to 2 decimal places.
# 7. Delete the to_fahrenheit() and to_celsius() functions.
# 8. In the temperature module, modify the code in the main() function so it tests
# the Temp class.
#     9. Run the temperature module. It should successfully convert the temperatures
# specified by the loops.
# Modify the program so it uses the Temp object
# 10. Switch back to the convert_temperatures.py file, and modify the import
# statement so it imports the Temp class from the temperature module.
# 11. In the convert_temp() function, create a Temp object and use it to set and get
# the temperatures.

from temperature import Temp

def display_menu():
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

def convert_temp():
    temp = Temp()
    option = int(input("Enter a menu option: "))
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = temp.setFahrenheit(f)
        c = temp.getCelsius(f)
        # c = temp.to_celsius(f)
        # c = round(c, 2)
        print("Degrees Celsius:", c)
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = temp.setCelsius(c)
        f = temp.getFahrenheit(c)
        # f = temp.to_fahrenheit(c)
        # f = round(f, 2)
        print("Degrees Fahrenheit:", f)
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
