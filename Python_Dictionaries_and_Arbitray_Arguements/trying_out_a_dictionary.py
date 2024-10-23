# A simple try on a dictionary
invetory = {
    "oranges": 1000,
    "mangoes": 2000,
    "apples": 4000,
}
sum_of_price = 0
for fruit in invetory:
    print(fruit)
print(dir(invetory))
print(invetory.get("oranges"))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
