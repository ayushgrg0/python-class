import os

print(os.getcwd())

filename = "platform_usage.py"
if os.path.exists(filename):
    print("Platform file exists.")
else:
    print("Platform file doesn't exists.")
