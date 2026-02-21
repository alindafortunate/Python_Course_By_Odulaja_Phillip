# A program to create a stand up meeting reminder.
# The meeting starts at 9:00am
# Steps
# Creating an email to send to the attendees.
# 1. The email message
# (1.From who, 2.To who, 3.Subject, 4.The message body, 5.An attachment 6.Scheduled time.)
# Resources
# (The 1.smtplib library, 2.SMTP_SSL class, 3.email module, 4.datetime module, 5.datetime class.)
import os
import smtplib
from smtplib import SMTP_SSL
from email.message import EmailMessage
from datetime import datetime
from datetime import time
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
OTHER_ADDRESS = os.environ.get("OTHER_ADDRESS")
PASSWORD = os.environ.get("EMAIL_PASSWORD")


def send_email():
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["TO"] = [EMAIL_ADDRESS, OTHER_ADDRESS]
    msg["Subject"] = "Code Review Meeting."
    msg.set_content(
        "Receive warm greetings dear Team, \nAs earlier communicated, we shall have our standup meeting on Saturday at 9:00am.\nAttend in person."
    )

    # Adding an attachment.
    with open(r"meeting_letter.txt", "rb") as letter:
        meeting_letter = letter.read()
        letter_name = letter.name
        msg.add_attachment(
            meeting_letter,
            maintype="application",
            subtype="octet-stream",
            filename=letter_name,
        )

    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, PASSWORD)
        server.send_message(msg)
        print("Email has been sent.")



schedule.every().saturday.at('13:25').do(send_email)
while True:
    schedule.run_pending()
    time.sleep(1)