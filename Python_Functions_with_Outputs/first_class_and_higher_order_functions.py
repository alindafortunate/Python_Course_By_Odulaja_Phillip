# A program to demostrate what the first class and a higher order function look like.


# first_class functions
def dog_sound():
    return "Woof!"


def cat_sound():
    return "Meow"


animal_sounds = [dog_sound, cat_sound]  # First class functions can be put into a list.
# for animal_sound in animal_sounds:
#     print(animal_sound())  # We are calling functions stored in a list.

# some thing to note importantly here is that
# we can do this
# bull_dog_sound = dog_sound
# print(
#     bull_dog_sound()
# )  # So you see here we assigned the dog_sound function to a variable bull_dog_sound.

# Example 01
# Higher order functions


def identify_animal_sounds(animal_sound):

    if animal_sound() == "Woof!":
        print("That animal is a dog.")
    else:
        print("That animal is a cat.")


identify_animal_sounds(dog_sound)


# Example 02
# Higher Order function for doubling values.
def double(n):
    return n * 2


def double_numbers(func, values):

    result = []
    for value in values:
        result.append(
            func(value)
        )  # Something note here is that, the double function will be called at this point.
    return result


doubled_digits = double_numbers(double, [3, 6, 7, 8, 9])
print(doubled_digits)


# def map_function(func, values):
#     result = []
#     for value in values:
#         result.append(func(value))
#     return result


# # using the custom map function
# doubled_values = map_function(double, [3, 6, 9, 12, 15])
# print(doubled_values)  # Output: [6, 12, 18, 24, 30]


# Example 03
def create_multiplier(factor):

    def multlpier(n):
        return n * factor

    return multlpier


double = create_multiplier(2)
trippled = create_multiplier(3)

print(double(5))
print(trippled(5))

def apply_to_each(func, iterable):
    return [func(x) for x in iterable]

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_each(square, numbers)
print(squared_numbers) # Output: [1, 4, 9, 16, 25]