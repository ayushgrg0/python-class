'''
Q1. Calculate string length.

Write a Python program to calculate the length of a string.
'''


def calculate_string(data):
    count = 0

    for char in data:
        count += 1

    return count


print(calculate_string("www.wikipedia.com"))

'''
Q2. Get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself
'''


def change_char(value):
    char = value[0]

    value = value.replace(char, '$')

    value = char + value[1:]

    return value


print(change_char('elephant'))

'''
Q3. Reverse a string

'''


def reverse_string(data):
    return ''.join(reversed(data))


print(reverse_string("Hello"))
