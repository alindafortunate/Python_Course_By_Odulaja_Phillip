# Working with python sets.
sports = set()
# print(type(sports))

set_functions = dir(sports)
# print(set_functions)

# "add", "clear", "copy", "difference", "discard", "intersection", "pop", "remove", "union", "update"

# Working with the add function.
item = "football"
item2 = "netball"
add_item = sports.add(item)
add_item2 = sports.add(item2)
# print(sports)

# Working with the clear function.

# clear_items = sports.clear()
# print(sports)

# Working with the copy functions
sports_copy = sports.copy()
# print(sports)
# print(sports_copy)

# Working with the difference function
vowels = {"a", "e", "i", "o", "u"}
alphabets = {
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
}
# difference = alphabets.difference(vowels)
# print(difference)

# Working with the discard function.
# discard_an_item = vowels.discard("b")
# print(vowels)

# Working with the intersection function.
# intersection = alphabets.intersection(vowels)
# print(intersection)

# Working with the pop function.
# vowels.pop()
# print(vowels)

commerce = {"Economics", "Entrepreneurship", "English", "Maths", "Commerce"}
stem = {"Maths", "Physics", "Chemistry", "English", "Science", "Biology"}


# Working with the remove function.
# remove_an_item = commerce.remove("Maths")
# print(commerce)

# Working with the union function.
union_set = commerce.union(stem)
print(union_set)

# Working with the update function.
Updated_commerce = commerce.update(stem)
print(commerce)
