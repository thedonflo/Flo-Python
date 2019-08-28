# def greet():
#     print("Hi there")
#     print("Welcome aboard")
#
# greet()

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
#
# greet("Funlola", "Ogunleye")


# def get_greeting(name):
#     return f"Hi {name}"
#
#
# message = get_greeting("Funlola")
#
# print(message)
#
# def increment(number, by):
#     return number + by
#
# print(increment(2, by=1))
# def increment(number, by=1):
#     return number + by
#
# print(increment(2))


# def multiply(*numbers):   #Creates tuples
#     print(numbers)
#
#
# multiply(2, 3, 4, 5)

# def multiply(*numbers):   #Creates tuples and iterates through them
#     for number in numbers:
#         print(number)
#
#
# multiply(2, 3, 4, 5)

# def multiply(*numbers):   #Creates tuples and iterates through them
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
#
# print(multiply(2, 3, 4, 5))

# def save_user(**user):  #Creates dictionary
#     print(user)
#     print(user["id"])
#     print(user["name"])
#
# save_user(id=1, name="John", age=22)


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


print(fizz_buzz(7))




