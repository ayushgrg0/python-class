"""
dictionary comprehension
"""

nums = [1, 2, 3, 4, 5, 6]
new_dict = {
    num: num + 100 for num in nums
}

print(new_dict)
