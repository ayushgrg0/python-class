
'''
Q1. Unique Numbers Check

Write a Python function that takes a sequence of numbers and determines whether all the
 numbers are different from each other.
'''


def unique_string(data):
    if len(data) == len(set(data)):
        print("The value stored are unique!!")
    else:
        print("The value are not unique!!")


data = [1, 21, 25, 51, 15, 14, 5, 2, 2]
unique_string(data)

'''
Q2. Random Even Number Generator

Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.
Note: Use random.sample() to generate a list of random values.
Sample Input:
(1,100)
Sample Output:
[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]
'''

even_numbers = []


for i in range(1, 20):
    if i % 2 == 0:
        even_numbers.append(i)
        print(even_numbers)
    else:
        print(" ")

'''
Q3. Generate List 1 to 10

Write a Python program to generate and print a list of numbers from 1 to 10.
Sample Input:
range(1,10)
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)
