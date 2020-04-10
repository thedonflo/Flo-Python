# 1. In IDLE, open the hangman.py file that's in this folder:
# python/ exercises/ ch10
# 2. Enhance this program so it displays a hangman graphic when the program
# starts as shown above. This hangman consists of the letter 0, bars, slashes,
# and backslashes. To display it, create a draw hangman() function that is called
# from the main() function.
# 3. Enhance this program so it adds one character to the hangman each time the
# player guesses wrong, starting with O for the head. To do this, enhance the
# draw hangman() function so it gets the number of wrong guesses as its only
# argument. Then, it should display that many hangman characters. This function
# should be called by the draw screen() function as well as the main() function.
# In this version of the game, the player only gets 7 wrong guesses. So, make
# sure to modify the program accordingly


import wordlist

# Get a random word from the word list
def get_word():
    word = wordlist.get_random_word()
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    hangman(num_wrong)
    print("-" * 79)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()

        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()

    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 7 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess

        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print("Congratulations! You got it in",
              num_guesses, "guesses.")
    else:
        print("Sorry, you lost.")
        print("The word was:", word)

def hangman(num_wrong=0):
    if num_wrong == 1:
        print("____")
        print("    |")
        print("    O")
    elif num_wrong == 2:
        print("____")
        print("    |")
        print("    O")
        print("    |")
    elif num_wrong == 3:
        print("____")
        print("    |")
        print("    O")
        print("   \\|")
    elif num_wrong == 4:
        print("____")
        print("    |")
        print("    O")
        print("   \\|/")
    elif num_wrong == 5:
        print("____")
        print("    |")
        print("    O")
        print("   \\|/")
        print("    |")
    elif num_wrong == 6:
        print("____")
        print("    |")
        print("    O")
        print("   \\|/")
        print("    |")
        print("   / ")
    else:
        print("____")
        print("    |")
        print("    O")
        print("   \\|/")
        print("    |")
        print("   / \\")


def main():
    print("Play the H A N G M A N game")
    hangman()
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()