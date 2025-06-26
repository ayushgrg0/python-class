import os

# CWD = current working directory

current_dir = os.getcwd()

print(f"Current Directory: {current_dir}")

# List files in directory

files = os.listdir('.')
print(f"Files in current directory: {files}")

# Create directory

if not os.path.exists('test_folder'):
    os.makedirs('test_folder')
    print("Directory created")
