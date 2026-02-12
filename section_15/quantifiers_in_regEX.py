# Working with groups and quantifiers.
import re

with open(r"text.txt", "r") as text_file:
    content = text_file.read()
    # matching usernames
    # pattern = re.compile(r"\B@\w+")

    # matching urls
    # pattern = re.compile(r"https?://(www\.)?\w+\.com")

    # matching phone numbers
    # pattern = re.compile(r"\+\d{1,3}\s\d+-\d+-\d+")

    # Matching ip addresses.
    # pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    # matching names with title like Mr, Mrs, Ms
    # Applying groups
    # pattern = re.compile(r"(Mr\.?|Ms\.?|Mrs\.?)\s[A-Za-z`+-_]+\s[a-zA-Z]+")

    # matching email addresses
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-z]+(\.com|\.org|\.edu)")
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
