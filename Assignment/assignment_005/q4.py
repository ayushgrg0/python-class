'''
Question 4. Inverted Centered Triangle Pattern

Task: Print an inverted centered triangle of stars with 5 rows.
Example Output:
*********
 *******
  *****
   ***
    *
'''


row = 5
for i in range(1, row + 1):
    spaces = " " * i
    stars = "*" * ((row * 2) - i)
    print(spaces + stars)
