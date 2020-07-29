import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fill in credentials here
# Make sure you have enabled access to less secure apps in your google profile. You can do it from here
# myaccount.google.com/lesssecureapps

def send_mail(username, password, subject, body=''):
    # Start connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to the server
    server.login(username, password)

    # Build message
    message = MIMEMultipart()

    # Check if message subject is provided
    # Set default if not provided: 'Demo Mail'
    if subject == '':
        subject = 'it is a test mail'

    message['From'] = username
    # Set recipient mail
    message['To'] = 'vikadie29@gmail.com'
    message['subject'] = subject

    if body == '':
        body = f'Hello! This email is sent from demo! {datetime.now()}'
    # Check if message body is provided
    # Set default if not provided: f'Hello! This email is sent from demo! {datetime.now()}'
    # Set provided message

    body = MIMEText(body)
    message.attach(body)

    # Send the mail
    server.send_message(message)
    print('Mail sent!')