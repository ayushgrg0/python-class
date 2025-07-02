'''
Question 3. **List Element Swapper (Lists and Loops)**
Write a function `swap_pairs(lst)` that takes a list and swaps every pair of adjacent elements.
If the list has an odd length, the last element remains in place. For example, `swap_pairs([1, 2, 3, 4])`
returns `[2, 1, 4, 3]`, and `swap_pairs([1, 2, 3])` returns `[2, 1, 3]`. Use list methods like indexing and loops.
'''

# a = 5
# b = 4
# print(a, b)

# # a, b = b, a
# print(b, a)


def swap_pairs(lst):
    for i in range(0, len(lst) - 1, 2):
        current_index = i
        next_index = i + 1
        lst[current_index], lst[next_index] = lst[next_index], lst[current_index]


print(swap_pairs([1, 2, 3, 4, 5, 6]))
