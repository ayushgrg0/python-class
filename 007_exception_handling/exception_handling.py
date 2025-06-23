'''
Q1. Handle IndexError in List Operations

Write a Python program that executes an operation on a list and handles an IndexError
exception if the index is out of range.
'''

# num = [1, 2, 3, 5, 6, 4]

# index = int(input("Enter the index:"))

# try:
#     result = num[index]
#     print(result)
# except IndexError:
#     print("Error: Index out of range.")


"""
Q2. Handle FileNotFoundError Exception When Opening a File

Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""
try:
    fp = open(r"C:\Users\USER\OneDrive\Desktop\python-class\007_exception_handling\hello.txt", "r")
    content = fp.read()
    print(content)
except FileNotFoundError as e:
    print(f"The error is {e}")


'''
Q3. Validate Integer Input and Raise ValueError

Write a Python program that prompts the user to input an integer and raises a ValueError
 exception if the input is not a valid integer.
'''
try:
    value = int(input("Enter a Number:"))
except ValueError:
    print("Error: Invalid input, input a valid integer.")
