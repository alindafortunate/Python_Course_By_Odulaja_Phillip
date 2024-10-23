# A program to work with the dict methods.

stock = {
    "electronic": 30,
    "furniture": 13,
    "books": 12,
    "math_books": 10,
}

# print(dir(stock))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
# get() method
# print(stock.get("books"))
# print(
#     stock["books"]
# )  # However its better to use this second method for its ability to catch errors.

# keys() method
# print(stock.keys())

# values() method
# print(stock.values())

# copy() method
# stock2 = stock.copy()
# print(stock2)
# print(stock)


# update() method

# stock.update({"books": 50})
# print(stock)

# clear method
# stock.clear()
# print(stock)

# pop method

# stock.pop("books")
# print(stock)

# popitem method
# stock.popitem()
# print(stock)
