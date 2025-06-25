'''
print the odd numbered fruits
'''


fruits = ["apple", "banana", "mango", "strawberry", "kiwi"]

for index, fruit in enumerate(fruits, start=1):
    if index % 2 != 0:
        print(f'{index}. {fruit}')


"""
list comprehension
"""
# square of list of numbers using list comprehension
nums = [1, 2, 3, 4, 5]

square_num = [num**2 for num in nums]

print(square_num)

# even numbers using list comprehension

nums = [1, 2, 3, 4, 5]

even_num = [num for num in nums if num % 2 == 0]

print(even_num)

# odd numbers using list comprehension

nums = [1, 2, 3, 4, 5]

odd_num = [num for num in nums if num % 2 != 0]

print(odd_num)
