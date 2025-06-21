

'''
Q1. Age group checker
WAP that takes the user's age as input.
Then prints whether the person is a:

Child (age < 13)

Teenager (13 - 19)

Adult (20-50)

Senior(60+)
'''

age = int(input("Enter your age:"))

if age < 13:
    print("You are a Child")

elif age >= 13 and age <= 19:
    print("You are a Teenager")

elif age >= 20 and age <= 50:
    print("You are a Adult")

elif age >= 60:
    print("You are a Senior")


"""
Q2. Number Operations
Tke two number from the user and display:

Their sum /n
Their difference /n
Their product /n

Whether the first number is divisible by the second number
"""

num1 = int(input("Enter your 1st number:"))

num2 = int(input("Enter your 2nd number:"))

print(f"The sum is {num1 + num2}")

print(f"The diff is {num1 - num2}")

print(f"The multiple is {num1 * num2}")

if num1 % num2 == 0:
    print("The first number is divisible by the second number")

else:
    print("The first number is not divisible by the second number")


"""
Q3. Odd or Even with a Twist /n
Take a number from the user. If it is even, print "Even number and its square is: "Followed by its square.""

If it is odd, print "Odd number and it's cube is: "Followed by its cube" "
"""


num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"Even number and it's square is : {num ** 2}")

else:
    print(f"Odd number and it's cube is : {num ** 3}")
