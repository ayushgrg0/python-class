'''
Q1. Handle IndexError in List Operations

Write a Python program that executes an operation on a list and handles an IndexError
exception if the index is out of range.
'''

num = [1, 2, 3, 5, 6, 4]

index = int(input("Enter the index:"))

try:
    result = num[index]
    print(result)
except IndexError:
    print("Error: Index out of range.")


'''
Q2. Handle ZeroDivisionError Exception

Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
'''
try:
    num = int(input("Enter a number"))
    result = 10 / num
    print(f'The result is {result}')
except ZeroDivisionError:
    print("The division by zero operation is not allowed.")


'''
Q3. Validate Integer Input and Raise ValueError

Write a Python program that prompts the user to input an integer and raises a ValueError
 exception if the input is not a valid integer.
'''
try:
    value = int(input("Enter a Number:"))
except ValueError:
    print("Error: Invalid input, input a valid integer.")
