# -*- coding: utf-8 -*-
"""codsoft.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H8_ploP1G3y5bwJdhZFYeB3q-AsSuIDO
"""

print("Calculator")


print("Enter the first number:")
a = float(input())
print("Enter the second number:")
b = float(input())
print("Enter the operator (1: +, 2: -, 3: *, 4: /):")
choice = input()


if choice == '1':
    result = a + b
    print("Result:", result)

elif choice == '2':
    result = a - b
    print("Result:", result)

elif choice == '3':
    result = a * b
    print("Result:", result)

elif choice == '4':
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid input")