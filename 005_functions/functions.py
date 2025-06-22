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


# perimeter = lambda a, b: 2 * (a + b)

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


'''
functions in a readable manner
'''


fruits = ["Apple"]


def display_menu():
    print("""
__________________MENU__________________
          1) Display fruits
          2) Add fruits
          3) Update fruits
          4) Delete fruits
          5) Exit
    """)


def display_fruits():
    for fruit in fruits:
        print(fruit)


def add_fruits():
    count = int(input("How many fruits do you want to add:"))
    for i in range(1, count + 1):
        fruit_name = input("Enter fruits")
        fruits.append(fruit_name)

    print("All the fruits are added successfully!!")


def update_fruits():
    display_fruits()
    update_index = int(input("Enter the index to update:"))
    update_value = input("Enter the updated fruit name")
    fruits[update_index] = update_value
    print("fruit successfully updated")


def delete_fruits():
    deletion_index = int(input("Enter the index to delete:"))
    fruits.pop(deletion_index)
    print(f"The item at index {deletion_index} is deleted")


while True:
    display_menu()

    user_choice = input("Enter the choice:")
    if user_choice == "1":
        display_fruits()

    elif user_choice == "2":
        add_fruits()

    elif user_choice == "3":
        update_fruits()

    elif user_choice == "4":
        delete_fruits()

    elif user_choice == "5":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
