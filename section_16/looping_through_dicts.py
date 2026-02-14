# Looping through dictionaries.
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8}

# Normal dict looping
for fruit in prices:
    print(fruit)  # Output is the dict keys e.g apple, banana. orange.


# If you want both keys and values, you can use:
# .items() – returns key-value pairs as tuples
# .values() – returns values
# .keys() – returns keys (same as default iteration)
