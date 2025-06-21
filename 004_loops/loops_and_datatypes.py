"""
Try guessing the lucky number

"""


while True:
    num = int(input("Enter the lucky number"))
    lucky_number = 7

    if num == lucky_number:
        print("You guessed the number. Congratulations!!")
        break


'''
using while loop adding value in a list
'''


while True:
    ask_user = int(input("How many fruits do you want to add:"))
    for i in range(0, ask_user):
        fruits = []
        user_input = input("Enter your favourite fruit:")
        fruits.append(user_input)
        print(fruits)
    break
