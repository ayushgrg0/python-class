'''
Q1. Sum Items in List
Write a Python program to sum all the items in a list.
'''

list_data = [1, 2, 3, 4, 5]
sum = 0

for i in list_data:
    sum += i

print(sum)

'''
Q2. Multiply all the items in a list
Write a Python program to multiply all the items in a list.
'''
another_data = [1, 2, 3, 4, 5]

multiple = 1

for i in another_data:
    multiple = multiple * i

print(multiple)

'''
Q3. Get Smallest Number in List

Write a Python program to get the smallest number from a list.
'''

number = [1, 285, 4, 7, 5241, 8, 21]

min = number[0]

for i in number:

    if i <= min:
        min = i
print(min)
