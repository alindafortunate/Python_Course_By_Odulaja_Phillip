# Working with json data into file
import json

data = {
    "name": "John Deo",
    "age": 30,
    "city": "New York",
    "email": "johndeo@example.com",
    "hobbies": ["reading", "traveling", "cooking"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "ABC University",
    },
}

# Serializing data into a file
# try:
#     with open(r"json_data.json", "x") as data_file:
#         json.dump(data, fp=data_file, indent=4)
# except FileExistsError:
#     print("File already exists.")

# deserializing data from a file.
try:
    with open(r"json_data.json", "r") as new_data:
        deserialised_data = json.load(new_data)
        print(deserialised_data)
except FileNotFoundError:
    print("File doesn't exist.")
