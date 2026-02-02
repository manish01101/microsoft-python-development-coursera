"""
There are different kinds of APIs. RESTful allows web services to communicate over HTTP by defining how things should be shown and manipulated. They are really flexible. Then there is SOAP and it is more rigid web communication that is used for systems that have high security levels. Lastly, GraphQL is perfect for apps with lots of data, allowing you to request just the specific information you need. It makes communication super efficient.
"""

# serialization(python dict to json)

import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)  # Serialize to JSON
print(data)
print(json_string)  # Output: {"name": "Alice", "age": 30}

# Setting timeouts for API requests
import requests

response = requests.get("https://api.example.com/data", timeout=10)

import requests

api_key = "YOUR_API_KEY"  # Replace with your actual API key
url = "https://api.weatherapi.com/v1/current.json"
params = {"key": api_key, "q": "London"}  # 'q' specifies the location

response = requests.get(url, params=params)
data = response.json()  # Convert the response to JSON format

print(data)


# jwt
import jwt

secret_key = "YOUR_SECRET_KEY"  # Keep this secret and secure!
payload = {"user_id": 123, "exp": 1633543343}  # 'exp' is the expiration timestamp

token = jwt.encode(payload, secret_key, algorithm="HS256")

print(token)


# illustrate the concept of messaging automation with a simple Python code snippet using the slack_sdk library for Slack.

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack configuration (replace with your actual token)
slack_token = "SLACK_BOT_TOKEN"
client = WebClient(token=slack_token)

# Channel ID where the bot will listen (replace with your channel ID)
channel_id = "YOUR_CHANNEL_ID"


# Simple chatbot logic
def handle_message(event):
    text = event["text"].lower()

    if "hello" in text:
        response = "Hi there! How can I help you today?"
    elif "weather" in text:
        # Here, you'd typically call an external weather API to fetch data
        response = "The weather in Wyoming, MI is currently sunny and 72°F."
    else:
        response = "I'm not sure I understand. Try asking me about the weather."

    try:
        client.chat_postMessage(channel=channel_id, text=response)
    except SlackApiError as e:
        print(f"Error posting message: {e}")


# Event listener (you'd typically integrate this with a Slack bot framework)
if __name__ == "__main__":
    # ... (Code to listen for incoming messages and call handle_message)
    print()


"""
Python's email libraries, like smtplib and imaplib,
"""
# smtplib focuses on sending email
import smtplib

# Replace with your email provider's SMTP server and your credentials
smtp_server = "smtp.your_email_provider.com"
smtp_port = 587  # Or the appropriate port for your provider
sender_email = "your_email@example.com"
sender_password = "your_password"

receiver_email = "recipient@example.com"
message = f"""\
Subject: Hello from Python

This is a test email sent from Python."""

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()


"""Constructing Email Messages with MIMEText
need a structured format (like a subject, sender, and recipient), it's best to use Python's email.mime.text.MIMEText class.

"""
from email.mime.text import MIMEText

# 1. Create the MIMEText object with the email body
message = MIMEText("This is the email body.")
# 2. Set the email headers like a dictionary
# The 'Subject' header defines the email's subject line.
message["Subject"] = "Your Custom Subject Here"
# The 'From' header specifies the sender's email address.
message["From"] = "sender@example.com"
# The 'To' header specifies the recipient's email address.
message["To"] = "recipient@example.com"
# Once configured, this 'message' object can be sent using server.send_message(message)
# from your smtplib.SMTP connection.


# imaplib gives the power to manage and interact with your inbox directly.
import imaplib

# Replace with your email provider's IMAP server and your credentials
imap_server = "imap.your_email_provider.com"
imap_port = 993  # Or the appropriate port for your provider
email_address = "your_email@example.com"
email_password = "your_password"

try:
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select("Inbox")

    status, messages = mail.search(None, "UNSEEN")
    if status == "OK":
        for num in messages[0].split():
            # Fetch the complete email data
            # (including headers and body) for each message
            # The data is fetched in RFC822 format, a text message standard
            status, data = mail.fetch(num, "(RFC822)")
            if status == "OK":
                # Process the email data (data[0][1]) here
                print("Fetched an unread email")
    else:
        print("Error searching for unread emails")

except Exception as e:
    print(f"Error fetching emails: {e}")
finally:
    # Close the connection and log out of the mail server
    mail.close()
    mail.logout()


"""
libraries like Tweepy, Instabot, and Facebook-sdk for seamless posting, data retrieval, and audience interaction

Scheduling tasks with Cron Jobs (Linux/macOS)
minute hour day-of-month month day-of-week command-to-be-executed
0 0 * * * /path/to/backup.sh
The 'minute' field accepts values from 0 to 59, enabling you to pinpoint the exact minute within an hour for your task to execute. The 'hour' field ranges from 0 to 23, with 0 representing midnight, providing flexibility in scheduling tasks throughout the day or night. For the 'day-of-month', you can specify values between 1 and 31, catering to monthly recurring tasks or specific dates. The 'month' field accepts either numerical values from 1 to 12 or their corresponding three-letter abbreviations (Jan-Dec), offering convenience in defining monthly or seasonal schedules. Lastly, the 'day-of-week' field ranges from 0 to 6, where 0 signifies Sunday, and you also have the option to use the abbreviations Sun-Sat, making it easy to schedule tasks on specific days of the week.

example
run a script at 10:30 AM every day => 30 10 * * * /path/to/script.sh
run a backup script at 2 AM every day => 0 2 * * * /path/to/backup.sh
execute a task on the 15th of every month => 0 0 15 * * /path/to/task.sh
run a script every January at midnight => 0 0 1 1 * /path/to/script.sh  or 0 0 1 Jan * /path/to/script.sh
run every Friday at noon => 0 12 * * 5 /path/to/task.sh

Special characters: Adding flexibility
The flexibility of cron is highlighted through its use of special characters, enabling you to craft intricate scheduling patterns. 
The asterisk (*) acts as a wildcard, representing all possible values within a field. For instance, an asterisk in the day-of-month field translates to "every day of the month". 
Commas (,) serve as separators for listing multiple specific values. So, '0,15,30,45' in the minute field signifies "every 15 minutes". 
Hyphens (-) come in handy for defining ranges. If you want a task to run on weekdays, you'd use '1-5' in the day-of-week field, indicating Monday through Friday.
Lastly, the slash (/) allows you to specify increments within a range. '/2' in the hour field means "every 2 hours". 

example
# Run a system check every 5 minutes
*/5 * * * * /usr/local/bin/system_check.sh
# Generate a sales report at 8 AM on the 1st and 15th of every month
0 8 1,15 * * /usr/local/bin/generate_sales_report.py
# Restart a service every weekday (Monday to Friday) at midnight
0 0 * * 1-5 /usr/local/bin/restart_service.sh
# Perform database maintenance every 4 hours 
0 */4 * * * /usr/local/bin/database_maintenance.sql
"""

"""
Python's schedule module: Simplified task scheduling

example
run every 2 seconds -> schedule.every(2).seconds.do(say_hello)
check_logs every 5 minutes -> schedule.every(5).minutes.do(check_logs)
run every Saturday => schedule.every().saturday.do(payroll)
run every Saturday at 11:30 PM => schedule.every().saturday.at("23:30").do(payroll)
every hour => schedule.every().hour

Tagging Jobs
The `tag(tag_name, ...)` method allows you to assign tags to scheduled jobs, making it easier to manage and identify them later.
schedule.every().day.at("00:00").do(backup_1).tag('maintenance')
schedule.every().sunday.do(defragment_disk).tag('maintenance')

Finding scheduled jobs
If your program has many tasks, you can use the `get_jobs()` method:
print(schedule.get_jobs())

get all tasks with a certain tag => print(schedule.get_jobs(tag='maintenance'))

If you need even more advanced options, the schedule module may not be for you. Other libraries such as `APScheduler` or `Celery` can be used to create complex schedules,

while True loop with time.sleep(1) is necessary in a Python script -> To prevent the script from exiting immediately after scheduling the task
"""
import schedule
import time


def say_hello():
    print("Hello, it's time for your scheduled task!")


def fetch_news_headlines():
    print("Fetching the latest news headlines...")
    # Add your actual news fetching logic here


def backup_data():
    print("Backing up your important data...")
    # Add your data backup logic here


# Schedule tasks
schedule.every().day.at("08:00").do(say_hello)  # Daily reminder at 8 AM
schedule.every(1).hour.do(fetch_news_headlines)  # Fetch news every hour
schedule.every().day.at("00:00").do(backup_data)  # Data backup at midnight

# Keep the script running to execute scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)

"""
import schedule

def send_daily_reminder():
    print("Don't forget to update the project status in the tracking tool!")

def send_weekly_reminder():
    print("Reminder: Weekly team meeting today at 9:00 AM!")

def calculate_volunteer_hours():
    print("Calculating volunteer hours. Results will be emailed!")

# Schedule the daily reminder for every day at 10 AM
### YOUR CODE HERE ###
schedule.every().day.at("10:00").do(send_daily_reminder).tag('reminders')

# Schedule the weekly reminder for every Monday at 9 AM
### YOUR CODE HERE ###
schedule.every().monday.at("09:00").do(send_weekly_reminder).tag('reminders')

# Schedule the volunteer hour calculations to be done at 11:59 PM Tuesday and Friday (2 lines of code)
### YOUR CODE HERE ###
schedule.every().tuesday.at('23:59').do(calculate_volunteer_hours)
### YOUR CODE HERE ###
schedule.every().friday.at("23:59").do(calculate_volunteer_hours)

print("Starting the reminder system...")
print("Currently scheduled tasks:")

# Print out current list of scheduled jobs
### YOUR CODE HERE ###
print(schedule.get_jobs())

# Instructions to start the scheduler
run_scheduler()
"""
