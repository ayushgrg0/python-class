"""
Q1. Sum All Numbers in a List

Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""


def sum_number(numbers):
    sum = 0

    for i in numbers:
        sum += i

    return sum


numbers = [8, 2, 3, 0, 7]
print(sum_number(numbers))


"""
Q2. Multiply All Numbers in a List

Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""


def multiple_number(numbers):
    multiple = 1

    for i in numbers:
        multiple *= i

    return multiple


numbers = [8, 2, 3, -1, 7]
print(multiple_number(numbers))


"""
Q3.  Print Even Numbers from a Given List

Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""


def even_numbers(sample_list):
    for i in sample_list:
        if i % 2 == 0:
            print(i)


even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
