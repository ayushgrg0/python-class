"""
Question 3. Centered Triangle (Pyramid) Pattern

Task: Print a centered triangle of stars with 5 rows, using spaces to align the stars.
Example Output
    *
   ***
  *****
 *******
*********
Hint: For each row, calculate the number of spaces needed before the stars to center the pattern,
and use an odd number of stars (1, 3, 5, etc.).

"""

num = 5
for i in range(num):
   print(f'Value of num ----> {num}')
   print(f' Value of i ---> {i}')
   spaces = num - i - 1
   print(f'Value of spaces ----->  {spaces}')
   stars = 2 * i + 1
   print(f'Value of stars --> {stars}')
   print(" " * spaces + stars * "*")


# print(" " * 5 + "-")
