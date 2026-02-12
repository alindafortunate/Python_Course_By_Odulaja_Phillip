# Working with groups and quantifiers.
import re

with open(r"text.txt", "r") as text_file:
    content = text_file.read()
    # matching usernames
    # pattern = re.compile(r"\B@\w+")

    # matching urls
    pattern = re.compile(r"https?://(www\.)?\w+\.com")
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
