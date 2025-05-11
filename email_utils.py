import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def init_email_session():
    try:
        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", "587"))
        email_user = os.environ.get("EMAIL_USER")
        email_password = os.environ.get("EMAIL_PASSWORD")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        return server
    except Exception as e:
        print(f"Email session error: {e}")
        return None

def send_mail(server, recipient, subject, body):
    email_user = os.environ.get("EMAIL_USER")
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server.sendmail(email_user, recipient, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Email sending failed: {e}")

def close_email_session(server):
    if server:
        server.quit()
