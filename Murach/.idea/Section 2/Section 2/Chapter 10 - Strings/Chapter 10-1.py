# 1. In IDLE, open the create_account.py file that's in this folder:
# python/ exercises/ ch10
# 2. Create and use a function to get a valid email address. To be valid, the address
# has to contain an @ sign and end with ".com".
#     3. Create and use a function to get a valid phone number. To do that, remove all
# spaces, dashes, parens, and periods from the number. Then, check to make
# sure it the phone number consists of 10 characters that are digits.
# 4. When all of the entries are valid, display the message shown above, including
# the phone number format that uses dots to group the digits.


def main():
    full_name = get_full_name()
    password = get_password()
    first_name = get_first_name(full_name)
    email = get_email()
    phone = phone_number()
    print()
    print("Hi " + first_name + ", thanks for creating an account.")
    print("We'll text your confirmation code to this number: "+phone)

def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip().replace(" ","")
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email address:       ").strip()
        if "@" in email  and email.endswith(".com"):
            return email
        else:
            print("Please enter a valid email address.")

def phone_number():
    while True:
        phone = input("Enter phone_number:       ").strip()
        #String formatting
        full_number = phone.replace(" ","").replace("(","").replace(")","").replace("-","")
        if len(full_number) == 10 and full_number.isdigit():
            phone_parse = full_number[:3]+"."+full_number[3:6]+"."+full_number[6:]
            return phone_parse
        else:
            print("Please enter a 10-digit phone number.")



if __name__ == "__main__":
    main()
