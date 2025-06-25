# from pprint import pprint


basic_info = {
    "name": "Ram",
    "age": 19
}

b_copy = basic_info.copy()

extra_info = {
    "nickname": "ramu",
    "name": "Shyam",
}


basic_info = basic_info | extra_info

print(basic_info)
print(b_copy)

# Convention experience aanusaar
# Rules
