# In this exercise, you'll modify the Movies List 2.0 program so it does more
# exception handling. You '11 also use a raise statement to test for exceptions.
# 1. In IDLE, open the movies2.py file that's in this folder:
# python/ exercises/ ch08
# 2. Add data validation to the add_movie() function so the year entry is a valid
# integer that's greater than zero. Then, test this change, and note that this
# creates a problem in the list_movies() function because the year needs to be
# converted to a string before it can be displayed. So, fix this and test again.
# 3. Modify the write_movies() function so it also handles any OSError exceptions
# by displaying the class name and error message of the exception object and
# exiting the program.
# 4. Test this by using a raise statement in the try block that raises a
# BlockingIOError. This is one of the child classes of the OSError. Then,
# comment out the raise statement.
# 5. In the read_movies() function, comment out the two statements in the except
# clause for the FileNotFoundError. Instead, use this except clause to return
# the empty movies list that's initialized in the try block. This should cause
# the program to continue if the file can't be found by allowing the program to
# create a new file for the movies that the user adds
# 6. Test this by first running the program with the same CSV file. That should
# work as before. Then, change the file name in the global constant to
# movies_test.csv, run the program again, and add a movie. That should create a
# new file. If that works, run the program again to check whether it works with
# the new file.

import csv
import sys

FILENAME = "movies.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()
    # except FileNotFoundError as e:
    #     print("Could not find " + FILENAME + " file.")
    #     exit_program()
    # except Exception as e:
    #     print(type(e), e)
    #     exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i in range(0, len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + " (" + movie[1] + ")")
    print()

def add_movie(movies):
    name = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
            if year > 0:
                break
            else:
                print("Entry must be greater than 0")
        except ValueError:
            print("You entered an invalid integer. Please try again")
    movie = []
    movie.append(name)
    movie.append(str(year))
    movies.append(movie)
    write_movies(movies)
    print(name + " was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. " +
                  "Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(movie[0] + " was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
