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

row = 5
for i in range(row, 0, -1):
    print("*" * i)
