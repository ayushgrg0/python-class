'''
Question 6. Hollow Right-Angle Triangle

Task: Print a hollow right-angle triangle with 5 rows, where only the border is made of stars.
Example Output:
*
**
* *
*  *
*****
'''


def print_hollow_triangle(rows: int) -> None:

    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print("*" * i)
        else:
            print("*", end="")
            hollow_space = i - 2
            print(" " * hollow_space, end="")
            print("*")


print_hollow_triangle(5)
