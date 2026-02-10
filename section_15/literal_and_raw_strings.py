# Using the regex functionality.
# We therefore have to import the re module and we can try to search through a sentence

# For that to work, we need a sentence but also a pattern object.
# On the pattern object we shall need a compile method from the re module to turn affect a raw string
# The raw string will have an r before it
# We shall then call the search method to help us on finding the pattern


import re

sentence = "I'am Alinda Fortunate, the best Software Developer in the world."
pattern = re.compile(r"Developer")
print(pattern.search(sentence))

# Below is a string and a raw string
print(
    "I am the best Software Developer in the world. \nAnd I serve Jesus Christ."
)  # A string

print(
    r"I am the best Software Developer in the world. \n And I serve Jesus Christ."
)  # A raw string because of the r before.

# When you print the above it's when they are best understood.