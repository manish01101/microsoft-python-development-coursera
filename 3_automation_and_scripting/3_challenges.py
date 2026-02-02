# Coding challenge: Send a confirmation email and check for replies
import smtplib
from email.mime.text import MIMEText
import imaplib

# Setup for email connection
smtp_server = "smtp.example.com"
smtp_port = 587
imap_server = "imap.example.com"
imap_port = 993
email_user = "orders@example.com"
email_password = "Coursera1000!"


def send_confirmation_email(client_email, client_name):
    # TODO: Add logic to send confirmation email
    server = None
    message = MIMEText(f"Thank you for your order, {client_name}!")
    message["Subject"] = "Order Confirmation"
    message["From"] = email_user
    message["To"] = client_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        # server.sendmail(email_user, client_email, message) #sendmail() expects a string, not a MIMEText object.
        server.send_message(message)
        print(f"Sent confirmation email to {client_name}!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        if server:
            server.quit()
    # pass


def check_new_messages(client_email, client_name):
    # TODO: Add logic to check for unread messages from the customer
    mail = None
    try:
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_user, email_password)
        mail.select("Inbox")

        status, messages = mail.search(None, f"UNSEEN FROM {client_email}")
        if status == "OK" and messages[0]:
            print(f"New message from {client_name}!")
        else:
            print("No new messages yet.")
    except Exception as e:
        print(f"Error checking messages: {e}")
    finally:
        if mail:
            mail.logout()

    # pass


# Example usage
client_email = "john.smith@example.com"
client_name = "John Smith"
send_confirmation_email(client_email, client_name)
check_new_messages(client_email, client_name)


"""
Challenge: Schedule product promotion posts
"""
import schedule
import time


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def promote_product():
    ### YOUR CODE HERE ###
    print(
        "Posting to Twitter: New product alert! Check out https://www.example.com/new-product #newproduct"
    )
    print(
        "Posting to Facebook: Our latest product is finally here! https://www.example.com/new-product"
    )


# Schedule the promotional social media posts for every day at 10 AM
### YOUR CODE HERE ###
schedule.every().day.at("10:00").do(promote_product)
# Schedule the promotional social media posts for every day at 4 PM
### YOUR CODE HERE ###
schedule.every().day.at("16:00").do(promote_product)

# Instruction to start the scheduler
run_scheduler()
