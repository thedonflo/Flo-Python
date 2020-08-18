# In this exercise, you'll enhance the Dice Roller pro grain by making some
# improvements to its classes.
# Open and test the program
# 1. In IDLE, open the dice.py and dice_roller.py files that are in this folder:
# python/ exercises/ ch14 / dice_roller
# 2. Review the code and run the program to make sure it works correctly. Note
# that it starts by displaying an image for each of the 6 possible die values.
# Improve the Die class
# 3. In the Die class, modify the roll() method so it returns the _ value attribute
# after it sets it to a random number from 1 to 6.
# 4. In the Die class, modify the constructor so it sets the _ value attribute by
# calling the roll() method. This makes sure that the _ value attribute for a new
# Die object stores a valid number for the die.
# 5. In the Die class, modify the setter for the value property so it doesn 't allow a
# value greater than 6.
# 6. Run the dice module and use Python 's interactive shell to make sure these
# changes work correctly.
# 7. In the Die class, add a read-only property named image that gets a string for
# the image that represents the die's current value.
# Improve the Dice Roller program
# 8. Open the dice_roller.py file and run it to make sure the Dice Roller program
# still works correctly. Since you didn 't change the interface for the Die class, it
# should.
# 9. Modify the code that displays the roll so it uses the new image property to
# display an image for each die instead of displaying the value.
# 10. At the start of the program, modify the code that displays the 6 die images so
# it uses a loop to create a Die object for each valid number and to display its
# image. This reduces code duplication since the code that defines the image is
# only stored in one place now, in the Die class.
# Improve the Dice class
# 11. In the Dice class, add a method named getTotal() that gets the total value of
# all Die objects currently stored in the Dice object.
# 12. In the dice_roller.py file, add the code that displays the total each time the
# user rolls the dice.

import random
from dice import Dice, Die

def main():
    print("The Dice Roller program")
    for i in range(1, 7):
        die = Die()
        die.value = i
        print(die.image)
    # print(" _____ \n" + \
    #       "|o   o|\n" + \
    #       "|o   o|\n" + \
    #       "|o___o|")
    # print(" _____ \n" + \
    #       "|o   o|\n" + \
    #       "|  o  |\n" + \
    #       "|o___o|")
    # print(" _____ \n" + \
    #       "|o   o|\n" + \
    #       "|     |\n" + \
    #       "|o___o|")
    # print(" _____ \n" + \
    #       "|o    |\n" + \
    #       "|  o  |\n" + \
    #       "|____o|")
    # print(" _____ \n" + \
    #       "|o    |\n" + \
    #       "|     |\n" + \
    #       "|____o|")
    # print(" _____ \n" + \
    #       "|     |\n" + \
    #       "|  o  |\n" + \
    #       "|_____|")

    print()

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    while True:
        # roll the dice
        dice.rollAll()
        # print("YOUR ROLL: ", end="")
        print("YOUR ROLL: \n")
        for die in dice.list:
            # print(die.value, end=" ")
            print(die.image)
        print("\n")

        choice = input("Roll again? (y/n): ")
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()


