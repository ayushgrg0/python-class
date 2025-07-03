'''
Question 10. Zigzag Pattern

Task: Print a zigzag pattern of stars across 5 rows, with stars forming a diagonal path.
Example Output:
*
   *
*
   *
*
Hint: Use a condition to place a star based on the row and column indices, creating a diagonal or alternating pattern.
'''

num = 5
space = 3

for i in range(num):
   if i % 2 == 0:
      print("*")
   else:
      print(" " * space + "*")
