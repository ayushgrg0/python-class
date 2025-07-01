'''
Question 6. **Longest Word Finder (Strings and Loops)**
Write a function `longest_word(sentence)` that takes a sentence and returns the longest word.
If multiple words have the same maximum length, return the first one. Use string methods like `split()` and a loop.
For example, `longest_word("I love programming")` returns `"programming"`.
'''


def longest_word(sentence):
    new = sentence.split()
    longest = ""
    max_length = 0
    for char in new:
        if len(char) > max_length:
            max_length = len(char)
            longest = char
    print(longest)


longest_word("I love programming")
