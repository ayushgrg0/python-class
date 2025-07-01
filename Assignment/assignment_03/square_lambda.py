'''
Question 7. Square Lambda
Define a lambda function that takes a number and returns its square. Assign it to a variable called square.
Example:

Input: square = lambda x: x * x; square(5)
Output: 25
Input: square(3)
Output: 9
'''

# def func(number):
#     square = number ** 2
#     return square

# lambda is an anonyms function

square = lambda num: num ** 2

print(square(5))
print(square(3))
