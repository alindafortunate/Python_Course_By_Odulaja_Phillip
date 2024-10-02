# working with the random module and the dir function.

# The dir function helps us to understand the functions present in a module.

import random

# import bank

# random_function = dir(random)
# bank_functions = dir(bank)
# print(random_function)
# print()
# print(bank_functions)

# working with
# choices, randint, random, shuffle, seed, randbyte

# names = ["Joan", "Pauline", "Leticia", "Sam", "Fortunate"]
# scores = [90, 98, 23, 45, 78, 89, 90, 99, 13, 47]

# random_score = random.choice(scores)
# random_name = random.choice(names)

# response = f"The random name is {random_name} and the random score is {random_score}"

# print(response)
# random_number = random.random()
# print(random_number)

random_integer = random.randint(1, 5)
print(random_integer)
