import random
keep_play = 'y'
while keep_play == 'y':
    random_number = random.randint(1, 10)
    #print(random_number)
    user_choice = 0
    while random_number != user_choice:
        user_choice = int(input("Guess a number between 1 and 10: "))
        if random_number < user_choice:
            print("Too high, try again")
        elif random_number > user_choice:
            print("Too low, try again")
        else:
            print("You guessed it! You won!")
    keep_play = input("Do you want to keep playing? (y/n) ").lower()
print("Okay, Good Bye!")


