# Use the locale module for the currency values
# 1. In IDLE, open the invoice_decimal.py file that's in this folder:
# python/ exercises/ ch09
# 2. Modify this program so it displays the order total and invoice total as currency
# values in the United States.

# Add a shipping cost
# 3. Add a shipping cost as shown in the console data above. This charge should
# be .085 of the subtotal. As a result, it could cause a rounding error. To prevent
# this error from occurring, use the decimal module to make sure each monetary
# value has the correct number of decimal places.
# 4. Test and debug this program and make sure that it works with all input values.

#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":

    # get user entry
    order_total = Decimal(input("Enter order total:     "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()

    # determine discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount
    shipping = Decimal(".085")
    shipping = subtotal * shipping
    shipping = shipping.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    invoice_total = subtotal + sales_tax + shipping

    # display the results
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")
    line = "{:20} {: >10}"
    # print("Order total:      {:10,}".format(order_total))
    print(line.format("Order total:",
                      lc.currency(order_total, grouping=True)))
    # print("Order total:      {:10,}".format(order_total))
    print(line.format("Discount amount:",discount))
    # print("Discount amount:  {:10,}".format(discount))
    print(line.format("Subtotal:",subtotal))
    # print("Subtotal:         {:10,}".format(subtotal))
    print(line.format("Shipping cost:",shipping))
    # print("Shipping cost:    {:10,}".format(shipping))
    print(line.format("Sales tax:",sales_tax))
    # print("Sales tax:        {:10,}".format(sales_tax))
    print(line.format("Invoice total:",
                     lc.currency(invoice_total, grouping=True)))
    # print("Invoice total:    {:10,}".format(invoice_total))
    print()

    choice = input("Continue? (y/n): ")
    print()

print("Bye")
