'''
Question 3. Greeting Message
Use string formatting to create a function greet_user that takes a name and an age and returns a string like
"Hello, [name]! You are [age] years old."
Example:

Input: greet_user("Alice", 25)
Output: "Hello, Alice! You are 25 years old."
Input: greet_user("Bob", 30)
Output: "Hello, Bob! You are 30 years old."
'''


def greet_user(name, age):
    print(f'Hello, {name}! You are {age} years old.')


greet_user("Alice", 25)
greet_user("Bob", 30)
