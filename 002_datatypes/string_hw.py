'''
Q1. Calculate string length.

Write a Python program to calculate the length of a string.
'''

data = "www.wikipedia.com"
print(len(data))


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
