

fp = open("introduction.txt", "w+")
fp.write("Hello, My name is Ayush.\n")
fp.write("I live in lekhnath \n")
fp.write("I like gaming and traveling.")
fp.seek(0)

lines = fp.readlines()
for line in lines:
    print(line, end="")
