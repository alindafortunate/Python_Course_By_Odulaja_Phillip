# Understanding how to search patterns in files
# by use of context managers.
import re

with open(r"text.txt", "r") as text:
    content = text.read()
    pattern = re.compile(r"\D\d\D\D\d\d\d\D\D\d")
    matches = re.finditer(pattern, content)

    for match in matches:
        print(match)
