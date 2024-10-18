# Working with the generator function.
# This is a type of function that has the "yield" key word.
# The main importantance of this function is to save memory since it keeps an at a time.

from typing import List


def divisor(numbers: List):
    """
    A function that divides a list by 2
    """
    result = []
    for num in numbers:
        new_number = num / 2
        result.append(new_number)
    return result


def divisor_gen(numbers: List):
    """
    A generator function that divides a list by 2
    """

    for num in numbers:
        new_number = num / 2
        yield new_number


weights = [90, 56, 43, 67, 34]
halved_weights = divisor(weights)
# print(halved_mylist) # Calling the normal function.

# Calling the generator function.
# print(divisor_gen(weights))  # Here it comes as an object.

# Using the next() to print out it's items.
gen_function = divisor_gen(weights)
# print(next(gen_function))
# print(next(gen_function))
# print(next(gen_function))

# Printing the item of the generator function using a for loop
# for y in gen_function:
#     print(y)

# converting the generator function back to a list.
# print(list(gen_function))
