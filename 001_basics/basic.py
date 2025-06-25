
'''
Word frequency counter
'''

line = input("Enter a sentence.")

words = line.split(" ")

# print(words)

counter_dict = {}

for word in words:
    # print(word)
    if word in counter_dict:
        # print(word)
        frequency = counter_dict[word]
        print(counter_dict[word])
        counter_dict[word] = frequency + 1
    else:
        counter_dict[word] = 1
        print(counter_dict)

print(counter_dict)


"""
Removing value from dictionary
"""


"""
list value even or odd in dictionary
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_dict = {}

for n in num:
    if n % 2 == 0:
        num_dict[n] = "even"
    else:
        num_dict[n] = "odd"
print(num_dict)
