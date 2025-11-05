#!/usr/bin/env python3

num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))

product = num1 * num2

print(f"{num1:g} x {num2:g} = {product:g}")

if product > 0:
    print("The result is positive.")
elif product < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")