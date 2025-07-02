'''
Question 1. Reverse a String
Write a function reverse_string that takes a string as input and returns the string reversed.
Example:

Input: reverse_string("hello")
Output: "olleh"
Input: reverse_string("Python")
Output: "nohtyP"
'''


def reverse_string(txt="hello"):
    return txt[::-1]


print(reverse_string())
print(reverse_string("Python"))
