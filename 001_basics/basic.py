
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
