# In this exercise, you'll convert the Movie List program presented in chapter 6 so
# it uses objects instead of storing the data for the movie in a list.
# Open and test the program
# 1. In IDLE, open the movie_list.py file that's in this folder:
# python/ exercises/ ch14 / movies
# 2. Review the code and note how it uses a list to store the data for each movie.
# 3. Run the code to make sure it works correctly.
# Define a Movie object that can store the data for each movie
#     4. Add a module named objects to the program's folder.
# 5. In the object module, write the code for a class named Movie that defines
# a Movie object that stores the name and year of a movie. This class should
#     include a getStr() method that returns the name of the movie followed by its
# year in parentheses.
# 6. Run the module. This should display the interactive shell. Then, use the shell
# to test the class by creating a Movie object and printing it to the console.
# Modify the program so it uses the Movie object
# 7. Switch back to the movie_list.py file, and add a statement that imports the
# Movie class.
#     8. Modify the main() function so it creates a list of Movie objects instead of a
# list of lists.
# 9. Modify the list() function so it uses the getStr() method to display each movie.
# Note how this simplifies the code.
# 10. Modify the add() function so it creates a Movie object from the user input.
# Note how this simplifies the code.
# 11. Modify the delete() function so it uses the Movie object to display the name
# of the movie that's deleted. Note how this makes the code easier to read and
# understand.

#!/usr/bin/env python3
from objects import Movie

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
        # for row in movie_list:
            print(str(i) + ". " + row.getStr())
            # print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
            i += 1
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    # movie = []
    # movie.append(name)
    # movie.append(year)
    movie = Movie(name,year)
    movie_list.append(movie)
    print(movie.getStr())
    # print(movie[0] + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie.getStr())        
        # print(movie[0] + " was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

def main():
    movie_list = [
        Movie("Monty Python and the Holy Grail", 1975),
        Movie("On the Waterfront", 1954),
        Movie("Cat on a Hot Tin Roof", 1958)]
    # movie_list = [["Monty Python and the Holy Grail", 1975],
                #   ["On the Waterfront", 1954],
                #   ["Cat on a Hot Tin Roof", 1958]]


    display_menu()

    while True:
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
