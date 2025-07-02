'''
Question 10. **List Range Filter (Lists, Loops, and Conditionals)**
Write a function `filter_range(lst, min_val, max_val)`
that takes a list of numbers and returns a new list containing
only the numbers within the range `[min_val, max_val]` (inclusive).
For example, `filter_range([1, 5, 3, 8, 2], 2, 5)` returns `[5, 3, 2]`.
Use list methods like `append()` and loops with conditionals.
'''


def filter_range(lst, min_val, max_val):
    new_lst = []
    for i in lst:
        if i >= min_val and i <= max_val:
            new_lst.append(i)
    print(new_lst)


filter_range([1, 5, 3, 8, 2], 2, 5)
