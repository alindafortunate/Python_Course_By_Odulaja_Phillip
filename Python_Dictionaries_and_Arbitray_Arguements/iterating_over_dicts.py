# A program to iterate through a dictionary.
stock = {
    "books": 30,
    "pens": 40,
    "pencils": 12,
    "rubbers": 30,
}

# looping through a dict.
# here we specify the key and the value
#
# for item, count in stock.items():
#     print(item)
#     print(count)

# for key, count in stock.items():
#     print(key)
#     print(count)

# looping through the keys.
# for key in stock.keys():
#     print(key)

# looping thorugh values.
# for value in stock.values():
#     print(value)

# items() method
stocked_items = stock.items()
print(stocked_items)
