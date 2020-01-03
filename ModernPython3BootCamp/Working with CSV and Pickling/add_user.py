# add_user
# For this exercise, you'll be working with a file called users.csv . ' \
#                       'Each row of data consists of two columns: a user's first name, and a user's last name.
#
# Implement the following function:
#
# add_user : Takes in a first name and a last name and adds a new user to the users.csv file.


from csv import writer


def add_user(firstname, lastname):
    with open("users.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([firstname, lastname])


add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson