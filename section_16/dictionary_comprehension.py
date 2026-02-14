# Working with dictionary comprehension.
# snytax

intended_dict = {"key": "value" for key in "value" if "pass"}
names = ["Ali", "Fortunate", "Mutesi"]

dict_of_names = {n: len(n) for n in names}
print(dict_of_names)

prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "mango": 1.23, "melon": 2.34}

expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 1.0}
print(expensive_fruits)
