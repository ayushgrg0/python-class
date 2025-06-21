user_1st_input = int(input("Enter 1st number:"))
operator = input("Enter a oprator '+,-,*,%,/':")
user_2nd_input = int(input("Enter 2nd number:"))

if operator == '+':
    operator = user_1st_input + user_2nd_input
    print(f"The sum of {user_1st_input} and {user_2nd_input} is {operator}")

elif operator == '-':
    operator = user_1st_input - user_2nd_input
    print(f"The difference of {user_1st_input} and {user_2nd_input} is {operator}")

elif operator == '*':
    operator = user_1st_input * user_2nd_input
    print(f"The multiplication of {user_1st_input} and {user_2nd_input} is {operator}")

elif operator == '/':
    operator = user_1st_input / user_2nd_input
    print(f"The division of {user_1st_input} and {user_2nd_input} is {operator}")

elif operator == '%':
    operator = user_1st_input + user_2nd_input
    print(f"The modulus of {user_1st_input} and {user_2nd_input} is {operator}")

else:
    print("Invalid operator")
