# Task: Given a list of names, create a new dictionary that groups the names
#  based on their first letter.
# The keys of the dictionary should be the first letters of the names,
#  and the values should be lists of names starting with that letter.

# Instructions:

# Write a function called group_names(names) that takes in a list of names as input.
# Inside the function, use a dictionary comprehension to create
# a new dictionary that groups the names based on their first letter.
# Return the resulting dictionary.
# Test your function with a sample list of names.

from typing import List

contacts = [
    "Emma",
    "Liam",
    "Olivia",
    "Noah",
    "Ava",
    "Isabella",
    "Sophia",
    "Jackson",
    "Luca",
    "Mia",
    "Charlotte",
    "Harper",
    "Evelyn",
    "Alexander",
    "James",
    "Benjamin",
    "Henry",
    "Ella",
    "Emily",
    "Michael",
]


def group_names(names: List):
    """
    This function returns groups of dictionaries with the key as the first letter and values as the names with the first letter
    """
    for n in names:
        n = names.index(n)

    groups = {
        name[0]: ()
        for name in names
    }
    return groups


print(group_names(contacts))
