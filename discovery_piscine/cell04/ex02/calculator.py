#!/usr/bin/env python3

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

print("Thank you!")

# Add subtract
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")

#Division + Conditioning logic for divide by 0
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:g}")
else:
    print(f"{num1} / {num2} = undefined (cannot divide by zero)")

#Multiplication
print(f"{num1} * {num2} = {num1 * num2}")