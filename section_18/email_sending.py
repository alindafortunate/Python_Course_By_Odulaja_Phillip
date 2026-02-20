# Working with email sending.

import os
import smtplib
from smtplib import SMTP


from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

with SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(
        EMAIL_ADDRESS,
        EMAIL_ADDRESS,
        "Subject : Testing Email Sending in Python \n\n Hello tyring to send an email with python.",
    )
    print("Email sent.")
