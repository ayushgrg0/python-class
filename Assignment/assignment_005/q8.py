'''
Question 8. Hollow Diamond Pattern

Task: Print a hollow diamond pattern with 5 rows in the upper half (total 9 rows),
where only the border is made of stars.
Example Output:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
Hint: Similar to the diamond pattern, but print stars only at the first and last positions of each row’s star sequence.
Manage spaces carefully.
'''

# first_num = 5
# second_num = 4
# for i in range(first_num):
#     spaces = first_num - i - 1
#     stars = 2 * i - 1
#     print(" " * spaces + "*" * stars)
# for i in range(second_num):
#     spaces = i
#     stars = 2 * (second_num - i) - 1
#     print(" " * spaces + "*" * stars)


num = 5

for i in range(num):
    spaces = num - i - 1
    print(" " * spaces, end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")

for i in range(num - 2, -1, -1):
    spaces = num - i - 1
    print(" " * spaces, end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")
