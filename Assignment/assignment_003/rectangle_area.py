'''
Question 5. Rectangle Area
Create a function rectangle_area that takes two parameters,
length and width (with width defaulting to 1), and returns the area of the rectangle.
Example:

Input: rectangle_area(5)
Output: 5
Input: rectangle_area(5, 3)
Output: 15
'''


def rectangle_area(length, width=1):
    area = length * width
    print(f'The area of the rectangle is {area}')


rectangle_area(5)
rectangle_area(5, 3)
