# Working with complex json data.
import json

with open(r"complex_json_data.json", "r") as json_data:
    data = json.load(json_data)
    # print(data)

    # iphone = data["store"]["departments"][0]['categories'][-1]['products'][0]
    nike_t_shirt = data['store']['departments'][1]['categories'][0]['products'][0]
    print(nike_t_shirt)
