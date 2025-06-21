user_age = int(input("Enter your age:"))

if (user_age > 18):
    print("Person is eble to vote.")
else:
    print("Incappable to vote.")

user_input = int(input("Enter a number"))

if user_input == 0:
    print("Number is 0")
elif user_input % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

user_value = int(input("Enter a number"))

if user_value % 5 == 0 and user_value % 7 == 0:
    print("Divisible by both 5 and 7")

elif user_value % 5 == 0:
    print("Divisible by 5")

elif user_value % 7 == 0:
    print("Divisible by 7")

else:
    print("Not divivsible by both")
