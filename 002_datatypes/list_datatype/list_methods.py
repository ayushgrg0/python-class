# Python List Methods
# ===================

# Lists are mutable (changeable) sequences in Python
# They have many built-in methods for manipulation

# 1. CREATING LISTS
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]
mixed = ["hello", 42, True, 3.14]
empty_list = []

print("Original fruits:", fruits)

# 2. ADDING ELEMENTS

# append() - Add ONE item to the end
fruits.append("orange")
print("After append:", fruits)

# insert() - Add item at specific position
fruits.insert(1, "grape")  # Insert at index 1
print("After insert:", fruits)

# extend() - Add MULTIPLE items to the end
more_fruits = ["kiwi", "mango"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# Alternatively, use += operator
fruits += ["pineapple", "strawberry"]
print("After += operator:", fruits)

# 3. REMOVING ELEMENTS

# remove() - Remove first occurrence of value
fruits.remove("banana")
print("After remove('banana'):", fruits)

# pop() - Remove and return item at index (default: last item)
last_fruit = fruits.pop()
print(f"Popped: {last_fruit}")
print("After pop():", fruits)

# Pop at specific index
second_fruit = fruits.pop(1)
print(f"Popped at index 1: {second_fruit}")
print("After pop(1):", fruits)

# del - Remove item at index (doesn't return value)
del fruits[0]
print("After del fruits[0]:", fruits)

# clear() - Remove all items
backup_fruits = fruits.copy()  # Make a copy first
fruits.clear()
print("After clear():", fruits)
fruits = backup_fruits  # Restore from backup

# 4. FINDING AND COUNTING

print("\nWorking with:", fruits)

# index() - Find index of first occurrence
cherry_index = fruits.index("cherry")
print(f"Index of 'cherry': {cherry_index}")

# count() - Count occurrences
fruits.append("apple")  # Add duplicate
apple_count = fruits.count("apple")
print(f"'apple' appears {apple_count} times")

# in operator - Check if item exists
if "mango" in fruits:
    print("We have mango!")
else:
    print("No mango found")

# 5. SORTING AND REVERSING

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nOriginal numbers:", numbers)

# sort() - Sort the list in place (modifies original)
numbers.sort()
print("After sort():", numbers)

# sort() with reverse=True
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)

# reverse() - Reverse the order
numbers.reverse()
print("After reverse():", numbers)

# 6. SORTING STRINGS
words = ["banana", "apple", "Cherry", "date"]
print("\nOriginal words:", words)

words.sort()  # Default: case-sensitive
print("After sort():", words)

# Case-insensitive sorting
words.sort(key=str.lower)
print("Case-insensitive sort:", words)

# 7. COPYING LISTS

original = [1, 2, 3, 4, 5]

# Shallow copy methods
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print("\nOriginal:", original)
print("Copy 1:", copy1)

# Modify original
original.append(6)
print("After modifying original:", original)
print("Copy remains unchanged:", copy1)

# 8. LIST COMPREHENSIONS (Creating new lists)
numbers = [1, 2, 3, 4, 5]

# Traditional way
squares = []
for num in numbers:
    squares.append(num ** 2)
print("\nSquares (traditional):", squares)

# List comprehension way
squares_comp = [num ** 2 for num in numbers]
print("Squares (comprehension):", squares_comp)

# With condition
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Even squares only:", even_squares)

# 9. NESTED LISTS (Lists containing lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix:", matrix)

# Access nested elements
print("Element at [1][2]:", matrix[1][2])  # Row 1, Column 2

# Flatten nested list
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
print("Flattened:", flattened)

# Or using list comprehension
flattened_comp = [item for row in matrix for item in row]
print("Flattened (comprehension):", flattened_comp)

# 10. PRACTICAL EXAMPLES

# Shopping list manager
shopping_list = []

# Add items
shopping_list.extend(["milk", "bread", "eggs"])
shopping_list.append("butter")
print("\nShopping list:", shopping_list)

# Check if we need something
if "milk" not in shopping_list:
    shopping_list.append("milk")

# Remove bought items
if "bread" in shopping_list:
    shopping_list.remove("bread")
    print("Bought bread!")

print("Updated shopping list:", shopping_list)

# 11. GRADES CALCULATOR
grades = [85, 92, 78, 96, 88, 90]
print(f"\nGrades: {grades}")

# Find statistics
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
print(f"Average grade: {sum(grades) / len(grades):.1f}")

# Count grades by category
a_grades = [grade for grade in grades if grade >= 90]
b_grades = [grade for grade in grades if 80 <= grade < 90]
c_grades = [grade for grade in grades if 70 <= grade < 80]

print(f"A grades: {len(a_grades)}")
print(f"B grades: {len(b_grades)}")
print(f"C grades: {len(c_grades)}")

# 12. COMMON PATTERNS

# Remove duplicates while preserving order
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = []
for num in numbers_with_dupes:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"\nUnique numbers: {unique_numbers}")

# Or using set and converting back (loses order)
unique_set = list(set(numbers_with_dupes))
print(f"Unique (using set): {unique_set}")

# Filter and transform
original_prices = [10.99, 25.50, 5.75, 30.00, 15.25]
# Apply 10% discount to items over $20
discounted = []
for price in original_prices:
    if price > 20:
        discounted.append(price * 0.9)  # 10% off
    else:
        discounted.append(price)

print(f"\nOriginal prices: {original_prices}")
print(f"After discount: {[f'${p:.2f}' for p in discounted]}")

print("\nLists are incredibly powerful and flexible in Python!")
