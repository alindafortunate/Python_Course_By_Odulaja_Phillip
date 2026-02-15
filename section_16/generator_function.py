# Working with generator functions


def generator_function():
    for n in range(1, 16):
        if n % 2 != 0:
            yield n


print(generator_function())  # This returns a generator object.

odd_numbers = generator_function()
print(
    next(odd_numbers)
)  # Using the next function helps us to see the values of the generator function
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(
    next(odd_numbers)
)  # To get other values, you call the next() function multiple times

# Working with generator expressions
# These ones are encosed in paranthesis () as opposed to list that are
# enclosed in square brackets []

odd_numbers = (n for n in range(1, 14) if n % 2 != 0)
print(next(odd_numbers))
