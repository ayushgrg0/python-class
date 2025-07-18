'''
Question 2. Palindrome Check
Create a function is_palindrome that takes a string and returns True if it is a palindrome
(reads the same forwards and backwards), False otherwise. Ignore case and non-alphabetic characters.
Example:

Input: is_palindrome("A man a plan a canal Panama")
Output: True
Input: is_palindrome("hello")
Output: False
'''


def is_palindrome(txt):
    cleaned_txt = ''
    for char in txt:
        if char.isalpha():
            cleaned_txt += char.lower()
    if cleaned_txt == cleaned_txt[::-1]:
        return True
    else:
        return False


print(is_palindrome("Malayalam"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))


# Approach 2

num = 12321

num_copy = num

reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    number = num // 10
print(f"{num_copy} is palindrom : {num_copy == reversed_num}")
