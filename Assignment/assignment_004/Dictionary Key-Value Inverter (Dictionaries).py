'''
4. **Dictionary Key-Value Inverter (Dictionaries)**
Write a function `invert_dict(d)` that inverts a dictionary, making keys into values and values into keys.
If multiple keys have the same value, group those keys in a list as the new value.
For example,`invert_dict({"a": 1, "b": 2, "c": 1})` returns `{1: ["a", "c"], 2: ["b"]}`.
Use dictionary methods like `items()` and loops.
.items() The items() method in Python dictionaries is used to
retrieve a view object that displays a list of key-value pair tuples
'''


def invert_dict(d):
    inverted_dict = {}

    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict


print(invert_dict({"a": 1, "b": 2, "c": 1}))
