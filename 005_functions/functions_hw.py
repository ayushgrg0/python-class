'''
Q1. Sum All Numbers in a List

Write a Python function to sum all the numbers in a list.
'''


def sum_number(numbers):
    sum = 0

    for i in numbers:
        sum += i

    return sum


numbers = [1, 2, 8545, 1548]
print(sum_number(numbers))


'''
Q2. Multiply All Numbers in a List

Write a Python function to multiply all the numbers in a list.
'''


def multiple_number(numbers):
    multiple = 1

    for i in numbers:
        multiple *= i

    return multiple


numbers = [1, 2, 8545, 1548]
print(multiple_number(numbers))
