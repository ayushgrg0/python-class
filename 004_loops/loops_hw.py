
"""
Q4. Sum of N natural numbers /n
Aske the user to enter a number n, and print the sum od the first n natural numbers using a loop

"""

n = int(input("Enter number:"))

sum = 0
for i in range(1, n + 1):
    print(f'Here is the values of i: {i}')
    sum = sum + i
    print(f'Here is the value of sum of natural numbers {sum}')


"""

Q5. Multiplication table generator

Ask the user to input a number. /n
Print it's multiplication table from 1 to 10.
"""


num = int(input("Enter a number"))
for i in range(1, 11):
    table = i * num
    print(f'{num} * {i} = {table}')


# print(f"{num*1}")
# print(f"{num*2}")
# print(f"{num*3}")
# print(f"{num*4}")


# print(f"{num*5}")
# print(f"{num*6}")
# print(f"{num*7}")
# print(f"{num*8}")
# print(f"{num*9}")
# print(f"{num*10}")
