

def get_float(prompt, low, high):
    while True:
        # get input from the user
        number = float(input(prompt))
        if low < number <= high:
            return number
        else:
            print("Entry must be greater than {} and less than or equal to {}".format(low, high))


def get_int(prompt, low, high):
    while True:
        # get input from the user
        number = int(input(prompt))
        if low < number <= high:
            return number
        else:
            print("Entry must be greater than {} and less than or equal to {}".format(low, high))


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        years = get_int("Enter number of years:\t", 0, 50)
        choice = input("Continue? (y/n): ")
    print()

    print("Bye!")


if __name__ == "__main__":
    main()

