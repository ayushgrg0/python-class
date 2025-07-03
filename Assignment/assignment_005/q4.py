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

num = 5

for i in range(num):
    stars = 2 * (num - i) - 1
    spaces = i
    print(" " * spaces + "*" * stars)
