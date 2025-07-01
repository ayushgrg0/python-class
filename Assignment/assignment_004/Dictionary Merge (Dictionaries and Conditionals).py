'''
Question 7. **Dictionary Merge (Dictionaries and Conditionals)**
Write a function `merge_dicts(dict1, dict2)` that merges two dictionaries.
If a key exists in both dictionaries, sum their values. For example, `merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})`
returns `{"a": 1, "b": 5, "c": 4}`. Use dictionary methods like `keys()` or `items()` and conditionals.
'''


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1


print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
