
''' r string
reading how to handle a file \n
printing a same data twice
 '''

fp = open(r"C:\Users\USER\OneDrive\Desktop\python-class\008_file_handling\Hello.txt", "r")
content = fp.read()
fp.seek(0)  # the seek funtion is used to move the file cursor to a specific position inside a file
print(content)

# printing the file again
value = fp.read()
print(value)
