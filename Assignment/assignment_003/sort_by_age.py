'''
Question 10. Sort by Age
Write a function sort_by_age that takes a list of tuples (name, age) and returns a new list
sorted by age in ascending order.Use a simple sorting algorithm (e.g., bubble sort) instead of sorted().
Example:

Input: sort_by_age([("Alice", 30), ("Bob", 25), ("Charlie", 35)])
Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
Input: sort_by_age([("Eve", 28), ("Dave", 40)])
Output: [("Eve", 28), ("Dave", 40)]
'''


def sort_by_age(infos: list[tuple[str, int]]) -> list[tuple[str, int]]:
    infos = sorted(infos, key=lambda item: item[1])
    return infos


people_info = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sort_by_age(people_info)
print(sorted_by_age)


nums = [4, 2, 5, 2, 6, 1]
print(sorted(nums, reverse=True))
