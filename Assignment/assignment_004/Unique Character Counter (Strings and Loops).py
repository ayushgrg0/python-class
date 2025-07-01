'''
Question 2. **Unique Character Counter (Strings and Loops)**
Create a function `unique_chars(text)` that takes a string and returns the count of unique characters
(case-sensitive) using a loop.
For example, `unique_chars("hello")` returns 4 (h, e, l, o are unique).
Avoid using sets; use a list to track characters and string methods like `in` for checking.
'''


# Approach 1
# def unique_chars(text):
#     char = len(set(text))
#     unique = set(text)
#     print(f'{char} {unique} are unique')


# unique_chars("hello")


# Approach 2
def unique_chars(text):
    unique_lst = []
    for char in text:
        if char not in unique_lst:
            unique_lst.append(char)
    print(len(unique_lst))


unique_chars("hello")
