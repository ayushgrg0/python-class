'''
Question 1
#  Extract all vowels from a string using list comprehension.
'''

# user_string = input("Enter a string: ")

# VOWEL_WORDS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# # A list comprehension generally follows this format:
# # [expression for item in iterable if condition]

# user_vowels = [i for i in user_string if i in VOWEL_WORDS]

# # for i in user_string:
# #     if i in VOWEL_WORDS:
# #         user_vowels.append(i)

# print(user_vowels)


'''
Question 2
#  Write a Python program using dictionary comprehension to filter Nepali students
# who scored more than 80 marks.
scores = {
    'Sita': 85,
    'Ram': 72,
    'Gita': 90,
    'Hari': 65,
    'Ayush': 95
}
'''

scores = {
    'Sita': 85,
    'Ram': 72,
    'Gita': 90,
    'Hari': 65,
    'Ayush': 95
}

# Dictionary Comprehension Syntax
# {key_expression: value_expression for item in iterable if condition}

more_than_80 = {name: marks for name, marks in scores.items() if marks > 80}

print(more_than_80)


'''
Question 3
converting 1D into 2D list
'''

num = [1, 2, 3, 4, 5, 6]

new_num = []
# new_num = [[for i in range(0, len(num), 2)], [num[i], num[i+1]]]

for i in range(0, len(num), 2):
    new = [num[i], num[i + 1]]
    new_num.append(new)

print(new_num)

'''
Question 4
Convert 2D list into 1D list
'''

num_2d = [
    [1, 2],
    [3, 4],
    [5, 6],
]

num_1d = []

for row in num_2d:
    print(row)
    for item in row:
        num_1d.append(item)

print(num_1d)

'''
Question 5
# Convert 2D list to 1D list with Help of list comprehesion
'''

two_d = [
    [1, 2],
    [3, 4],
    [5, 6],
]

one_d = [item for row in two_d for item in row]

print(one_d)


'''
Question 6
WAP to find the table of number from the data provide by the user
'''

number = int(input("Enter a number"))

for i in range(1, 11):
    table = i * number
    print(f'{i} * {number} = {table}')

'''
Question 7

Write a Python program using list comprehension that takes a number as input from the user
and prints the multiplication table of that number
'''

number = int(input("Enter a number: "))


table = [f'{i}* {number} = {number * i}' for i in range(1, 11)]

print(table)
