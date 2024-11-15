# Hi, this script's objective is to receive an input number then show pi's n digit based on numbers provided.

import math

# Input the number with "int" telling the number format
n = int(input("Insert digit:"))

# "n" equals the number of decimals you want to show while "math.pi" pulls the numbers from math library
pi = round(math.pi, n)

# Display the final result
print("The value of π (pi) is:", pi)
