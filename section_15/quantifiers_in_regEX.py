# Working with groups and quantifiers.
import re

with open(r"text.txt", "r") as text_file:
    content = text_file.read()
    # matching usernames
    # pattern = re.compile(r"\B@\w+")

    # matching urls
    # pattern = re.compile(r"https?://(www\.)?\w+\.com")

    # matching phone numbers
    pattern = re.compile(r"\+\d{1,3}\s\d+-\d+-\d+")
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
