# Exploring how to work with serious data that we want to remain hidden.
# We shall be using the python dotenv library for this case.

import os
from dotenv import load_dotenv

load_dotenv()


# working with envirinment variable from the .env file.
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
name = os.environ.get("name")


# output of the environment variables.
print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)
print(name)
