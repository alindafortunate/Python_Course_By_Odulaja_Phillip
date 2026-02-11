# Understanding how to search patterns in files
# by use of context managers.
import re

with open(r"text.txt", "r") as text:
    content = text.read()
    # pattern = re.compile(r"\D\d\D\D\d\d\d\D\D\d") # Digits and None digits.
    # word boundary
    # pattern = re.compile(r"\bhello")

    # matching usernames.
    pattern = re.compile(r"\B@\w\w\w\w\w\w\w")
    matches = pattern.finditer(content)

    for match in matches:
        print(match)
