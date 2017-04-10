#!/usr/bin/env python3
#import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

def send_email(dest, textfile):
    """
    Sends an email containing a plain textfile as the body
    Args:
        dest -> where to send the email
        textfile -> the text file containing the desired body text
    """
    with open(textfile) as fp:
        # Create a text/plain message
        msg = MIMEText(fp.read())
            
            # me == the sender's email address
            # you == the recipient's email address
        msg['Subject'] = 'HW8 Progress Report'
        msg['From'] = 'hw8Email@gmail.com'
        msg['To'] = dest
            
            # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()


def main():
    #send_email('', 'test.txt')
    pass

if __name__ == "__main__":
    main()
    exit(0)

