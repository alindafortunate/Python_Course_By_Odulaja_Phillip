# Understanding dict comprehession.
prices = {"apple": 2.3, "banana": 3.4, "mango": 0.89, "pawpaw": 0.7}

cheap_fruits = dict(filter(lambda item: item[1] < 1.00, prices.items()))
print(cheap_fruits)

# Recommended approach is dictionary comprehension
cheap_fruits = {fruit: price for fruit, price in prices.items() if price < 1.0}
print(cheap_fruits)
