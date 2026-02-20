# Working with email sending.

import os
import smtplib
from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

msg = EmailMessage()
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg["Subject"] = "Trying the Email Module."
msg.set_content("Wow I am making progress.")
with SMTP_SSL("smtp.gmail.com", 465) as server:
    # server.ehlo()
    # server.starttls()   # Here we are going to use SMPT_SSL to replace the security these three lines would enforce.
    # server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(
        msg
    )  # When using the email module you now use the send_message() function to send the email.
    print("Email sent.")
