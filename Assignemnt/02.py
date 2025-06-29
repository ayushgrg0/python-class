def display_menu():
    print("""
-------------------- Menu --------------------
            1. Display menu
            2. Display the fruit list
            3. Simple Calculator
            4.
            5. Guess the Number
            6. About the temperature
            7. Even or Odd
            8. Display all the files

    """)


'''
Question 1: Favorite Fruit List
Create a list of your 5 favorite fruits (as strings, like "apple" or "banana"). Then:

Print the entire list.
Print the first and last fruit in the list.
Add a new fruit to the list using the append() method and print the updated list.
'''


def fruits():
    my_fav_5_fruits = ['apple', 'banana', 'orange', 'mango', 'grape']
    print(f'The list of fruits are: {my_fav_5_fruits}')
    print(f'The 1st fruit is {my_fav_5_fruits[0]}, and the last fruit is {my_fav_5_fruits[-1]}')

    my_fav_5_fruits.append('strawberry')
    print(f'The updated fruit list is {my_fav_5_fruits}')


'''
Question 2: Simple Calculator
Ask the user to input two numbers (use input()). Then:

Add the two numbers together and print the result.
Multiply the two numbers and print the result.
Make sure to convert the inputs to numbers (use float() or int()) so you can do math with them!
'''


def calculator():
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))

    sum = num1 + num2
    product = num1 * num2

    print(f'The sum of the 2 numbers provided are: {sum}')
    print(f'The product of the 2 numbers provided are: {product}')

# '''
# Question 3: Counting Stars
# Write a program that uses a for loop to print the numbers 1 to 10,
# and for each number, print that many stars (*). For example, for the number 3, print ***.
# '''


"""
Question 4: Guess the Number
Write a program that asks the user to enter a number between 1 and 10 using a while loop.
Keep asking until they enter a number in that range. Once they do, print "Great choice!" and stop.
"""


def guess():
    while True:
        user = int(input("Enter a number between 1 to 10: "))
        if user > 0 and user <= 10:
            print("Great Choice!")
            break
        else:
            print("That's not the number between 1 to 10")


"""
Question 5: Weather Advice
Ask the user to input the current temperature (as a number). Then:

If the temperature is above 30, print "It's hot! Wear sunglasses!"
If the temperature is between 15 and 30 (inclusive), print "It's nice outside! Enjoy!"
If the temperature is below 15, print "It's cold! Wear a jacket!"
"""


def temperature():
    temp = int(input("Enter the current temperature :"))
    if temp > 30:
        print("It's hot! Wear sunglasses!")
    elif temp >= 15 and temp <= 30:
        print("It's nice outside! Enjoy!")
    elif temp < 15:
        print("It's cold! Wear a jacket!")


"""
Question 6: Even or Odd
Ask the user to input a number.
Use an if statement to check if the number is even or odd, and print the result.
(Hint: A number is even if number % 2 == 0.)
"""


def even_or_odd():
    user = int(input("Enter a number: "))

    if user % 2 == 0:
        print("The given data is an even number!")
    else:
        print("The given data is a odd number!")


"""
Question 7: List Your Files
Write a program that uses the os module to list all the files in the current folder (use os.listdir()).
Print each file name on a new line.
"""

import os


def files():
    files = os.listdir()
    # print(f"------------> 'Files in the current directory': {files}")
    for file in files:
        print(f"Files in the current directory: {file}")
