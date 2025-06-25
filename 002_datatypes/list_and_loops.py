# lists and loops

# Creating a new list
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

print("Working with Lists and Loops")
print("=" * 30)

# Display the list
print("My fruit list:")
print(fruits)
print()

# Loop through the list

print("Looping through each fruit")
for fruit in fruits:
    print(f"- {fruit}")

print()

# loop with index
print("Fruits with their position:")
for i in range(len(fruits)):
    print(f"{i + 1}. {fruits[i]}")

print()

# Create a list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through numbers

print("Numbers from 1 to 10")
for num in numbers:
    print(num, end=" ")

print("\n")
print("Lists and loops demonstration completed!")
