def Calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2

    elif operator == '-':
        return num1 - num2

    elif operator == '*':
        return num1 * num2

    elif operator == '/':
        return num1 / num2

    else:
        return None


sum = Calculator(5252, '+', 78451)
print(f"The sum is {sum}")

diff = Calculator(525458952, '-', 78451)
print(f"The difference is {diff}")

multi = Calculator(5244452, '*', 78451)
print(f"The multiplication is {multi}")

division = Calculator(5254152, '/', 78451)
print(f"The division is {division}")


'''
basic operations using functions
'''


def perimeter(a, b):
    return 2 * (a + b)


def circle_area(radius, pi=3.14):     # default parameter
    return pi * (radius ** 2)


print(circle_area(4, pi=4))    # keyword parameter


perimeter = lambda a, b: 2 * (a + b)

print(perimeter(4, 9))


def greeting(name, greet):
    return f'{greet}!. How are you {name}?'


print(greeting("Ayush", "Hello"))


def calculate(a, b):
    sum_result = a + b
    product = a * b
    return sum_result, product


result = calculate(2, 3)
print(result)

total, multiplication = calculate(4, 5)
print(f'Sum : {total}, Product : {multiplication}')
