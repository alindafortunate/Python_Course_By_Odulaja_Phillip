# Working with complex json data.
import json

with open(r"complex_json_data.json", "r") as json_data:
    data = json.load(json_data)
    print(data)
