# Working with the shuffle and seed functions

# The seed function initialises a rondom value and makes it static in that even if you run the program many times you get the same value

# The shuffle function just shuffles the values in a given iterable.

import random

plants = ["coffee", "matooke", "cocoa", "avocado"]
gardens = [1, 2, 3, 4]

# seed function
# random.seed(1)
# random_plant = random.choice(plants)
# random_garden = random.choice(gardens)


# shuffle function
random.shuffle(plants)
random.shuffle(gardens)

print(plants)
print(gardens)
