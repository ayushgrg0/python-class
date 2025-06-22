
import json

file_path = r"C:\Users\USER\OneDrive\Desktop\python-class\.vscode\extensions.json"
with open(file_path, "r") as fp:
    read_json = fp.read()
    content_dictionary = json.loads(read_json)
    print(content_dictionary)
    print(content_dictionary["recommendations"][0])
