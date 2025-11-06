#!/usr/bin/env python3

stringin = input("Give me a number: ")

try:
    num = float(stringin)
    
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("That's not a number! Try again.")