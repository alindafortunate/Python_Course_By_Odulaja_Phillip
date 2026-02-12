# Working with groups and quantifiers.
import re

with open(r"text.txt", "r") as text_file:
    content = text_file.read()
    # pattern to match usernames easily
    pattern = re.compile(r"\B@\w+")
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
