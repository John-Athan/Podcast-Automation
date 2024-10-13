import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_link(file_link):
    sender_email = os.getenv("EMAIL")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    subject = "Your Podcast Episode is Ready"
    body = f"Here is the link to your podcast episode: {file_link}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
    server.starttls()
    server.login(sender_email, os.getenv("PASSWORD"))

    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
