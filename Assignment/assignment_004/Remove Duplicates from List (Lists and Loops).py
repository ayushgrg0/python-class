'''
Question 5. **Remove Duplicates from List (Lists and Loops)**
Write a function `remove_duplicates(lst)` that removes duplicates from a list while preserving the original order.
Do not use sets. For example, `remove_duplicates([1, 3, 3, 4, 1, 5])` returns `[1, 3, 4, 5]`.
Use list methods like `append()` and a loop to check for duplicates.
'''


def remove_duplicates(lst):
    no_duplicates = []
    for i in lst:
        if i in no_duplicates:
            pass
        else:
            no_duplicates.append(i)
    return no_duplicates



print(remove_duplicates([1, 3, 3, 4, 1, 5]))
