'''
Question 2. Inverted Right-Angle Triangle Pattern

Task: Print an inverted right-angle triangle of stars with 5 rows.
Example Output:
*****
****
***
**
*

Hint: Decrease the number of stars from 5 to 1 as the row number increases.
'''

num = 6
for row in range(num, 0, - 1):
    print(row * "*")
