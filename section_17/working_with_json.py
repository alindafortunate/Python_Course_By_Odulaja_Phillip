# Working with json data in Python
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

# # Encoding/Serialising data into json format
# serialised_data = json.dumps(data, indent=4)
# print(serialised_data)
# print(type(serialised_data))

# # Deserialising data from json back to python dict
# deserialised_data = json.loads(serialised_data)
# print(deserialised_data)