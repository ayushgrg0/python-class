'''
Q1. Write a python program to display all the prime numbers from 1 to 50
'''
# num = int(input("Enter a number"))

# is_prime = True
# for i in range(2, num - 1):
#     if num < 2:
#         continue
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime number')


for num in range(1, 50):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=",")


'''
Q2. Write a python program that takes a list of words adn groups them based on their length.
Th elenght should create a dictionary where:
    - The keys are the lengths of the words (as numbers),
    - The values are lists of words having that length
Finally, print the dictionary.

Example:
words = ['apple', 'dog', 'banana' , 'car' , 'car', 'mango',]

Expected Output:
{
    5: ['apple', 'Mango']
    3: ['dog', 'car', 'cat']
    6: ['banana']'


}
'''

# words = 'apple' 'dog' 'banana' 'car' 'car' 'mango'
# print(words)
words = ['apple', 'dog', 'banana', 'car', 'car', 'mango']

print(len(words))

word_dict = {}

for word in words:
    print(len(word))
    if len(word) in word_dict:
        word_dict[len(word)].append(word)
        # print(word_dict)
    else:
        word_dict[len(word)] = [word]
        print(word_dict)

print(word_dict)

# How is a new list created?
# 🟢 English:
# When you write [word], you're using square brackets to create a new list — and you're putting the word inside that list.

# So for example, if the word is 'banana', then:

# [ 'banana' ]   # This is a list with 1 element
# You're assigning that list to a new key in the dictionary like this:

# word_dict[6] = ['banana']
# → Now the dictionary has a new key 6, and the value is a list containing 'banana'.

# 🔵 Nepali Roman:

# [word] le garda tyo word ekdamai naya list bhitra halincha.

# Jasto ki:

# [ 'car' ]
# bhaneko chai ek ota list ho, jas ma euta matra word cha: 'car'.

# Tyes list lai:


# word_dict[len(word)] = [word]
# le garda dictionary ma tyo list add huncha as a value under the key of len(word).

# 🧠 Example Breakdown:
# Suppose:


# word = 'car'
# len(word) = 3
# Since 3 is not yet in the dictionary:


# word_dict[3] = ['car']
# Now word_dict becomes:

# {3: ['car']}
# If next word is 'dog':

# len('dog') = 3

# Since 3 is already a key now:

# word_dict[3].append('dog')
# Now it becomes:

# {3: ['car', 'dog']}

'''
Q3. Write a program that groups them in a dictionary based on the first letter of each name:

Example Input:

names = [
    "Mundre", "Magne Buda", "Jire Khursani", "Mundre Junior", "Gaida", "Magne",
    "Chankhe", "Dhurmus", "Suntali", "Pooja Sharma", "Junu", "Bale",
    "Chankhe Junior", "Phool Baje", "Takme Buda", "Kale Dai", "B.K.",
    "Sakal", "Dhurmus Junior", "Rajaram", "Thakur", "Suntali Junior"
]


Expected Ouput
{
    'M': ['Mundre', 'Magne Buda', 'Mundre Junior', 'Magne'],
    'J': ['Jire Khursani', 'Junu'],
    'G': ['Gaida'],
    'C': ['Chankhe', 'Chankhe Junior'],
    'D': ['Dhurmus', 'Dhurmus Junior'],
    'S': ['Suntali', 'Sakal', 'Suntali Junior'],
    'P': ['Pooja Sharma', 'Phool Baje'],
    'T': ['Takme Buda', 'Thakur'],
    'K': ['Kale Dai'],
    'B': ['Bale', 'B.K.'],
    'R': ['Rajaram']
}

'''

names = [
    "Mundre", "Magne Buda", "Jire Khursani", "Mundre Junior", "Gaida", "Magne",
    "Chankhe", "Dhurmus", "Suntali", "Pooja Sharma", "Junu", "Bale",
    "Chankhe Junior", "Phool Baje", "Takme Buda", "Kale Dai", "B.K.",
    "Sakal", "Dhurmus Junior", "Rajaram", "Thakur", "Suntali Junior"
]

names_dict = {}

for name in names:
    if name[0] in names_dict:
        names_dict[name[0]].append(name)
    else:
        names_dict[name[0]] = [name]

print(names_dict)
