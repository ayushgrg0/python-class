
''' r string
reading how to handle a file /n
printing a same data twice
 '''

fp = open(r"C:\Users\USER\OneDrive\Desktop\python-class\008_file_handling\Hello.txt", "r")
content = fp.read()
fp.seek(0)
print(content)

value = fp.read()
print(value)
