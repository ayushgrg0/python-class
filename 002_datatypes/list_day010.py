'''
print the odd numbered fruits
'''


fruits = ["apple", "banana", "mango", "strawberry", "kiwi"]

for index, fruit in enumerate(fruits, start=1):
    if index % 2 != 0:
        print(f'{index}. {fruit}')
