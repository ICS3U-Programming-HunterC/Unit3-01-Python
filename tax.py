#!/usr/bin/env python3

# Created by: Hunter Connolly
# Created on: March 25, 2022
# This program calculates total from subtotal and British Colombia tax


import constants


def main():
    # this function calculates the total from subtotal and tax

    # Get the subtotal from the user (input)
    print("Today we will calculate the total of your items using British\
 Colombia tax rates")
    sub_total = float(input("Enter the subtotal: $"))

    # Calculate the tax and subtotal (process)
    tax = sub_total * constants.HST_BC
    total = sub_total + tax

    # Display the tax and total to the user (output)
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: \
${1:,.2f}" .format(tax, total))


if __name__ == "__main__":
    main()
