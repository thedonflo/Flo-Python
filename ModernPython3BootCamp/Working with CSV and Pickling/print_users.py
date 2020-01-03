# print_users
# For this exercise, you'll be working with a file called users.csv . ' \
#                       'Each row of data consists of two columns: a user's first name, and a user's last name.
#
# Implement the following function:
#
# print_users : prints out all of the first and last names in the users.csv file


from csv import reader, DictReader


#list version
def print_users():
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for name in csv_reader:
            print(("{} {}").format(name[0], name[1]))

#Dictionary version
# def print_users():
#     with open("users.csv") as csvfile:
#         csv_reader = DictReader(csvfile)
#         for row in csv_reader:
#             print("{} {}".format(row['First Name'], row['Last Name']))


print_users()