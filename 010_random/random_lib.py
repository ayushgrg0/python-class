import random

# Random integers
dice_roll = random.randint(1, 6)
print(f'Dice roll: {dice_roll}')
print("=" * 30)

# # Random float between 0 and 1
# probability = random.random()  # for float data
# print(f"Random probability: {probability:.4f}")
# print("=" * 30)

# # Random choice from list
# colors = ['red', 'green', 'blue', 'yellow']
# random_color = random.choice(colors)
# print(f"Random color: {random_color}")
# print("=" * 30)


# # Shuffle a list
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(f"Shuffled numbers: {numbers}")
# print("=" * 30)

# # Random sample (multiple choices without replacement)
# sample = random.sample(colors, 2)
# print(f"Random sample: {sample}")
# print("=" * 30)


roll_dice = int(input("How many times do you want to roll the dice? : "))

for i in range(roll_dice):
    value = random.randint(1, 6)
    print("The value of the dice rolled: ", value)


nice_compliments = [
    "You are awesome.",
    "I'm grateful to know you.",
    "You're a great listener.",
    "I appreciate you",
    "You light up the room",
]

random_compliments = random.choice(nice_compliments)
print(random_compliments)
