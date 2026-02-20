# Working with email sending.

import os
import smtplib
from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage
import imghdr

from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

msg = EmailMessage()
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg["Subject"] = "Sky Diving Competition."
message_body = """
Hello, the Lord is good to me and I know that surely He will give me a way out each and every day of my life.

We are excited to announce our very first sky diving contest that will happen in Mbarara.
"""
msg.set_content(message_body)
images = ["sky_diving 2.jpg", "sky_diving.jpg"]
for image in images:
    with open(image, "rb") as file:
        image_file = file.read()
        image_name = file.name
        image_format = imghdr.what(image_name)
    msg.add_attachment(
        image_file, maintype="image", subtype=image_format, filename=image_name
    )


with SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)
    print("Email sent.")
