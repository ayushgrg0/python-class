
name = input("Enter your name : ")

VOWEL_LETTERS = ["a", "e", " i", "o", "u"]

user_vowels = []

for i in name:  # Assignment
    if i in VOWEL_LETTERS:  # Membership checker
        user_vowels.append(i)

print(user_vowels)
