import os

# Current working directory
current_dir = os.getcwd()
print(f"-------> 'Current directory': {current_dir}")
print("-" * 70)
# List files in directory

files = os.listdir()
print(f"------------> 'Files in the current directory': {files}")
print("-" * 70)


# Create directory
if not os.path.exists("new_test_folder"):
    os.makedirs("new_test_folder")
    print("Directory created")
else:
    print("Directory already exists!!")
print("-" * 70)


# Environment variables

home_dir = os.environ.get("HOME", "Not found")
print(f"Home directory: {home_dir}")
print("-" * 70)

# File operations
file_path = "new_test_folder"
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")
else:
    print("File doesn't exist")
