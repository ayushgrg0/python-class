def display_menu():
    print('''
-------------------- Menu --------------------
            1. Display menu
            2. Display the fruit list
            3. Simple Calculator
            4.
            5. Guess the Number

    ''')


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
