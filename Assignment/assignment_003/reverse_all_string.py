'''
Question 13. Reverse All Strings
Write a function reverse_all that takes a list of strings and returns a new list where each string is reversed.
Example:

Input: reverse_all(["hello", "world"])
Output: ["olleh", "dlrow"]
Input: reverse_all(["python", "code"])
Output: ["nohtyp", "edoc"]
'''


def reverse_all(word_lst):
    new_lst = []
    for word in word_lst:
        reversed_word = word[::-1]
        new_lst.append(reversed_word)
    print(new_lst)


reverse_all(["hello", "world"])
reverse_all(["python", "code"])
