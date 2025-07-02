'''
Question 4. Vowel Counter
Write a function count_vowels that takes a string and returns the number of vowels
(a, e, i, o, u, both lowercase and uppercase) in it.
Example:

Input: count_vowels("Hello World")
Output: 3
Input: count_vowels("PYTHON")
Output: 1
'''

vowels = ["a", "e", "i", "o", "u"]


def count_vowels(txt):
    cleaned_txt = ''
    for char in txt:
        cleaned_txt += char.lower()

    count = 0
    for i in cleaned_txt:
        if i in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))
print(count_vowels("PYTHON"))
