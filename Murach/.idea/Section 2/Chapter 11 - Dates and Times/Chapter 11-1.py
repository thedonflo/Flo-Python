# Review the code and make sure it works correctly
# 1. In IDLE, open the invoice.py file that's in this folder:
# python / exercises/ch11
# 2. Review the code and run the program to see how it works.
# Use date objects to store the three dates
# 3. Modify the get_invoice_date() function so it uses a four-digit year.
# 4. Modify the program so it uses date objects, not datetime objects, to store
# the three dates. To do that, you can create a date object from the parts of the
# datetime object that's created in the get_invoice_date() function.
# Add validation
# 5. Run the program, and enter an invalid date. This should cause the program
# to crash. Then, add code to the get_invoice_date() function that prevents the
# program from crashing and makes sure the user enters a valid date.
# 6. Add code to the get_invoice_date() function that makes sure the user enters a
# date that's either today or in the past.

#!/usr/bin/env python3

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:
        try:
            invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
            return invoice_date

        except ValueError:
            print("Invalid date format! Try again.")

def main():
    print("The Invoice Due Date program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()
        invoice_date = date(invoice_date.year,invoice_date.month,invoice_date.day)
        if invoice_date <= date.today():
            invoice_date
        else:
            print("Date must be today or earlier. Try again.")
            continue

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date:     " + due_date.strftime("%B %d, %Y"))
        print("Current Date: " + current_date.strftime("%B %d, %Y"))
        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")
        print()

        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
