import feedparser
import time
import smtplib
from email.message import EmailMessage

# Email configuration
sender_email = 'sridharkonda43@gmail.com'
receiver_email = 'sreedhar4343@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sridharkonda43@gmail.com'
smtp_password = 'diwfasgvppxidzhi'

# URL of the Shopify API Changelog RSS feed
feed_url = 'https://shopify.dev/changelog/feed.xml'

# Function to send email notification
def send_notification(title, published_date, link):
    msg = EmailMessage()
    msg['Subject'] = 'Shopify API Deprecation Notification'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    message = f"Title: {title}\nPublished Date: {published_date}\nLink: {link}"
    msg.set_content(message)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

# Function to check for deprecated APIs
def check_for_deprecations():
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)
    keywords = ["Online Store", "Algolia Search and Discovery", "ScriptEditor", "Metafields Guru", "Email", "admin-graphql"]
    # Check if there are any entries (updates)
    if len(feed.entries) > 0:
        # Loop through each entry to find deprecated APIs
        for entry in feed.entries:
            # Check if the entry contains deprecated API information
            if 'deprecated' in entry.title.lower():

#             if any(keyword in entry.title.lower() for keyword in keywords) and 'deprecated' in entry.title.lower():
                # Send email notification
                send_notification(entry.title, entry.published, entry.link)

# Run the script every 1 hour
while True:
    check_for_deprecations()
    time.sleep(36000)  # Sleep for 10 hour (3600 seconds)