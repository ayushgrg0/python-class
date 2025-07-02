'''
Question 1. Right-Angle Triangle Pattern

Task: Write a Python program to print a right-angle triangle of stars with 5 rows.
Example Output:
*
**
***
****
*****
Hint: Use a single for loop to control the number of stars in each row, increasing from 1 to 5.
'''

# a = "*"
# print(a)

num = 6
for row in range(1, num):
    print(row * "*")
