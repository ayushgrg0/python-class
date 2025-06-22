

import json

# file_path = r"C:\Users\USER\OneDrive\Desktop\python-class\.vscode\extensions.json"

# with open(file_path, "r") as fp:

#     read_json = fp.read()

#     content_dictionary = json.loads(read_json)

#     print(content_dictionary)

#     print(content_dictionary["recommendations"][0])


content = '{"Name": "Ayush", "Age": "19", "Address": "Lekhnath", "Number": "984546563"}'
print(type(content))

content_dict = json.loads(content)
print(type(content_dict))
key_value_pairs = content_dict.items()  # dictionary method 'item'
print(key_value_pairs)

for key, value in key_value_pairs:
    print(key, value)
