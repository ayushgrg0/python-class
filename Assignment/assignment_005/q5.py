'''
Question 5. Diamond Pattern

Task: Print a diamond pattern of stars with 5 rows in the upper half (total 9 rows).
Example Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
Hint: Combine the logic of a centered triangle (increasing stars) and an inverted centered triangle (decreasing stars).
Use two separate loops or a conditional approach.
'''

first_num = 5
second_num = 4
for i in range(first_num):
    spaces = first_num - i - 1
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
for i in range(second_num):
    spaces = i
    stars = 2 * (second_num - i) - 1
    print(" " * spaces + "*" * stars)
