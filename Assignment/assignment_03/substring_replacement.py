'''
Question 12. Substring Replacement
Create a function replace_substring that takes three strings: the original string, the substring to replace,
and the replacement string. Return the modified string with all occurrences of the substring replaced.
Example:

Input: replace_substring("hello world", "world", "Python")
Output: "hello Python"
Input: replace_substring("cat cat dog", "cat", "bird")
Output: "bird bird dog"
'''


def replace_substring(original, to_replace, replacement):
    result = original.replace(to_replace, replacement)
    print(result)


replace_substring("hello world", "world", "Python")
replace_substring("cat cat dog", "cat", "bird")
