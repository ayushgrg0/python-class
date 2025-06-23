'''
Q1. Add Key to Dictionary

Write a Python program to add a key to a dictionary.
'''

data = {"Name": "Shyam", "Hobby": "Drawing", "Height": "5.6 ft"}

print(data)

data.update({"Location": "Syangja"})

print(data)

'''
Q2. Merge Two Python Dictionaries

Write a Python script to merge two Python dictionaries.
'''

dic1 = {"Name": "Ram", "Age": 20}
dic2 = {"Hooby": "Coding", "Height": 5.9}

dic3 = dic1.copy()

print(dic3)

dic3.update(dic2)

print(dic3)


'''
Q3. Sum All Items in a Dictionary

Write a Python program to sum all the items in a dictionary
'''

data = {"data1": 101, "data2": 202, "data3": 303}

sum = sum(data.values())

print(sum)
