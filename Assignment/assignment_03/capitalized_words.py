'''
Question 11. Capitalize Words
Write a function capitalize_words that takes a sentence (a string) and returns a new sentence
where the first letter of each word is capitalized.
Example:

Input: capitalize_words("hello world")
Output: "Hello World"
Input: capitalize_words("python is fun")
Output: "Python Is Fun"
'''

'''
To capitalize the first letter of every word in a string in Python,
the most straightforward and recommended method is to use the built-in str.title() method.
'''


def capitalize_words(data):
    new_data = str.title(data)
    print(new_data)


capitalize_words("hello world")
capitalize_words("python is fun")
