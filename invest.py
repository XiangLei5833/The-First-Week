#!/usr/bin/env python3

amount = float(input("Enter amount: "))
incrate = float(input("Enter Interest rate: "))
period = float(input("Enter period: "))

value = 0
year = 1

while year <= period:
    value = amount + (incrate*amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1
