import os
import platform

print(os.getcwd())

system = platform.system()

if system == "Darwin":
    print("Rich")
elif system == "Linux":
    print("Developer")
elif system == "Windows":
    print("Under rich")
