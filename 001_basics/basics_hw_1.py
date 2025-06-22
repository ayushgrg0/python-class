'''
Q1. Conditional Sum to 20

Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
'''


def sum(a, b):
    sum = a + b

    if sum >= 15 and sum <= 20:
        return 20
    else:
        return sum


print(sum(2, 10))
print(sum(10, 5))
print(sum(19, 1))


# num1 = int(input("Enter the 1st number:"))
# num2 = int(input("Enter the 2nd number:"))

# sum = (num1 + num2)
# if sum >= 15 and sum <= 20:
#     print("20")
# else:
#     print(sum)


'''
Q2. Triangle Area Calculator

Write a Python program that will accept the base and height of a triangle and compute its area.
'''


# def triangle_area_calculator(base: int, height: int):
#     area = (base * height) / 2
#     print(f'The area of the triangle is {area}')


# base = int(input("Enter the value for base:"))
# height = int(input("Enter the value for height:"))

# triangle_area_calculator(base, height)


'''
Height to Centimeters

Write a Python program to convert height (in feet and inches) to centimeters.

Future Value Calculator

Write a Python program to compute the future value of a specified principal amount, \n
rate of interest, and number of years. \n
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''


def future_value(amount, interest, years):
    total = amount * (1 + interest) / years
    print(f'The future value is {total}')


future_value(10000, 3.5, 7)
