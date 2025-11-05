#!/usr/bin/env python3

# import sys script to deal with arguments

import sys

# halts the main thing and print none if supplied with argument

if len(sys.argv) > 1:
    print("none")
    sys.exit()

# if input doesnt have any argument

i = 0

while i <= 10:
    print(f"Table de {i}:", end=" ")
    m = 0

    while m <= 10:
        print(i * m, end="")
        if m < 10:
            print(" ", end="")
        m += 1
    print()
    i += 1